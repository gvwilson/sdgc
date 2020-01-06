#!/usr/bin/env python

import argparse
import io
import json
import os
import random
import re
import string
import subprocess
import sys
import yaml

PARSER = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'md2ast.rb')

#--------------------------------------------------------------------------------

def clean(text):
    '''LaTeX escape special characters.'''
    for (src, dst) in [('_', r'\_'), ('&', r'\&'), ('#', r'\#')]:
        text = text.replace(src, dst)
    return text


def makeHyperlink(href, contained):
    '''Create a hyperlink based on the text of the link target.'''

    # Link in text <http://something.something>
    if href == contained:
        href = clean(href)
        result = f'\\url{{{href}}}'

    # Bibliography citation [Key,Key](BIB)
    elif href == 'BIB':
        result = f'\\cite{{{contained}}}'

    # Figure reference [f:key](FIG)
    elif href == 'FIG':
        result = f'\\figref{{{contained}}}'

    # Glossary entry: text contained [text][key], but 'key'
    # was in glossary table and translated to '../glossary/#key'.
    elif '/glossary/' in href:
        chapter, term = href.split('#')
        result = f'\\gref{{g:{term}}}{{{contained}}}'

    # Cross-references to chapters always start with '.' or '..'
    elif href[0] == '.':
        # Refers to section
        if '#' in href:
            chapter, section = href.split('#')
            result = f'{contained} (\\secref{{{section}}})'
        # Refers to chapter only
        else:
            chapter = href.strip('.').strip('/')
            result = f'{contained} (\\chapref{{s:{chapter}}})'

    # Cross-references to sections within a chapter start with '#'
    elif href[0] == '#':
        result = f'{contained} (\\secref{{{href[1:]}}})'

    # Pure and simple link to the outside world.
    else:
        href = clean(href)
        result = f'\\hreffoot{{{href}}}{{{contained}}}'

    return result


def nodesToText(children, slug):
    '''Convert all child nodes to text, returning a list for further processing.'''
    children = [HANDLERS[child['type']](child, slug, io.StringIO())
                for child in children]
    children = [child.writer.getvalue()
                for child in children]
    return children


class Handler(object):
    '''Base class for element handlers.'''

    def __init__(self, node, slug, writer):
        '''
        Store the node, the slug of the file, and the output stream,
        then start this element, process children, and finish this element.
        '''
        self.node = node
        self.slug = slug
        self.writer = writer
        self.start()
        self.children()
        self.finish()

    def start(self):
        '''Generate text for start of element.'''
        pass

    def children(self):
        '''Process children (if any).'''
        if 'children' in self.node:
            for child in self.node['children']:
                if child['type'] not in HANDLERS:
                    print('UNKNOWN TYPE', child, file=sys.stderr)
                else:
                    HANDLERS[child['type']](child, self.slug, self.writer)

    def finish(self):
        '''Generate text for end of element.'''
        pass


class Anchor(Handler):
    '''Handle <a>.'''

    def start(self):
        '''Do all processing here.'''
        href = self.node['attr']['href']
        contained = ''.join(nodesToText(self.node['children'], self.slug))
        hyperlink = makeHyperlink(href, contained)
        self.writer.write(hyperlink)

    def children(self):
        '''Suppress the usual child processing.'''
        pass


class Blank(Handler):
    '''Handle blank lines.'''

    def start(self):
        self.writer.write('\n')


class Blockquote(Handler):
    '''Handle blockquotes.'''

    def start(self):
        self.writer.write('\\begin{quote}\n')

    def finish(self):
        self.writer.write('\\end{quote}\n')


class Break(Handler):
    '''Handle explicit line breaks.'''
    pass


class CodeBlock(Handler):
    '''Handle code blocks.'''

    def start(self):
        if ('attr' not in self.node) or ('class' not in self.node['attr']):
            print('NO CODE CLASS', self.node, file=sys.stderr)
            return

        language = self.node['attr']['class'].replace('language-', '')
        self.writer.write(f'\\begin{{minted}}{{{language}}}\n')
        self.writer.write(self.node['value'])
        self.writer.write('\\end{minted}\n')


class CodeSpan(Handler):
    '''Handle inline code spans.'''

    def start(self):
        text = clean(self.node["value"])
        self.writer.write(f'\\texttt{{{text}}}')


class DefinitionDef(Handler):
    '''Handle definition bodies.'''

    def start(self):
        pass

    def finish(self):
        self.writer.write('\n')


class DefinitionList(Handler):
    '''Handle overall definition list.'''

    def start(self):
        self.writer.write('\\begin{description}\n')

    def finish(self):
        self.writer.write('\\end{description}\n')


class DefinitionTermDefault(Handler):
    '''Handle definition terms in normal contexts.'''

    def start(self):
        self.writer.write('\\item[')

    def finish(self):
        self.writer.write(']')


class DefinitionTermGlossary(Handler):
    '''Handle definition terms for glossary entries.'''

    def start(self):
        label = self.node['attr']['id']
        self.writer.write(f'\\gitem{{{label}}}{{')

    def finish(self):
        self.writer.write('}')


class Emphasis(Handler):
    '''Handle inline emphasis.'''

    def start(self):
        self.writer.write('\\textit{')

    def finish(self):
        self.writer.write('}')


class Header(Handler):
    '''Handler headers.'''

    LEVELS = ['', 'chapter', 'section', 'subsection', 'subsubsection']

    def start(self):
        '''Open the section heading.'''
        level = self.LEVELS[self.node['options']['level']]
        self.writer.write(f'\n\\{level}{{')

    def finish(self):
        '''Close the section heading and add a label if present.'''
        self.writer.write('}')
        if ('attr' in self.node) and ('id' in self.node['attr']):
            label = self.node['attr']['id']
            self.writer.write(f'\\label{{{label}}}')


class HTML(Handler):
    '''Fallback for HTML elements that Kramdown can't convert.'''

    def start(self):
        '''Switch on element type, saving any post text in member variables.'''
        self.after = None
        value = self.node['value']
        if value == 'sup':
            self.writer.write(f'\\textsuperscript{{')
            self.after = '}'
        else:
            print('UNKNOWN HTML', self.node, file=sys.stderr)

    def finish(self):
        '''Add post text if any.'''
        if self.after is not None:
            self.writer.write(self.after)


class ListItem(Handler):
    '''Handle list item.'''

    def start(self):
        self.writer.write('\n\\item ')


class Math(Handler):
    '''Handle math section.'''

    def start(self):
        self.writer.write(self.node['value'])


class OrderedList(Handler):
    '''Handle ordered list.'''

    def start(self):
        self.writer.write('\\begin{enumerate}\n')

    def finish(self):
        self.writer.write('\n\\end{enumerate}\n')


class Paragraph(Handler):
    '''Handle paragraph.'''

    def start(self):
        self.writer.write('\n')

    def finish(self):
        self.writer.write('\n')


class Root(Handler):
    '''Handle root of document.'''
    pass


class SmartQuote(Handler):
    '''Handle smart quotes (basically by ignoring them).'''

    QUOTES = {
        'ldquo': '"',
        'lsquo': "'",
        'rdquo': '"',
        'rsquo': "'"
    }

    def start(self):
        actual = self.QUOTES[self.node['value']]
        self.writer.write(f'{actual}')


class Strong(Handler):
    '''Handle bold text.'''

    def start(self):
        self.writer.write('\\textbf{')

    def finish(self):
        self.writer.write('}')


class Table(Handler):
    '''Handle tables.'''

    ALIGNMENT = {
        'default': 'l',
        'left': 'l',
        'right': 'r'
    }

    def start(self):
        alignment = self.node['options']['alignment']
        alignment = [self.ALIGNMENT[a] for a in alignment]
        alignment = ''.join(alignment)
        self.writer.write(f'\\begin{{tabular}}{{{alignment}}}\n')

    def finish(self):
        self.writer.write('\\end{tabular}\n')


class TableBody(Handler):
    '''Handle table body.'''

    pass


class TableHead(Handler):
    '''Handle table head.'''

    pass


class TableRow(Handler):
    '''
    Handle table row by capturing and formatting children.
    This is needed to ensure there are only '&' between columns and not at the end.
    '''
    def children(self):
        cells = [node for node in self.node['children'] if node['type'] == 'td']
        cells = nodesToText(cells, self.slug)
        self.writer.write(' & '.join(cells) + ' \\\\\n')


class TableData(Handler):
    '''Do nothing special for table cells (handled by row handler).'''
    pass


class Text(Handler):
    '''Handle plain old text.'''

    def start(self):
        text = clean(self.node['value'])
        self.writer.write(text)


class TypographicSymbol(Handler):
    '''Handle typographic symbols.'''

    SYMBOLS = {
        'hellip': r'{\ldots}',
        'mdash': '---'
    }

    def start(self):
        value = self.node['value']
        if value in self.SYMBOLS:
            self.writer.write(self.SYMBOLS[value])
        else:
            print('UNKNOWN SYMBOL', self.node, file=sys.stderr)


class UnorderedList(Handler):
    '''Handle unordered list.'''

    def start(self):
        self.writer.write('\\begin{itemize}\n')

    def finish(self):
        self.writer.write('\n\\end{itemize}\n')


HANDLERS = {
    '_root': Root,
    'a': Anchor,
    'blank': Blank,
    'blockquote': Blockquote,
    'br': Break,
    'codeblock': CodeBlock,
    'codespan': CodeSpan,
    'dd': DefinitionDef,
    'dl': DefinitionList,
    'dt': DefinitionTermDefault,
    'em': Emphasis,
    'header': Header,
    'html_element': HTML,
    'li': ListItem,
    'math': Math,
    'ol': OrderedList,
    'p': Paragraph,
    'smart_quote': SmartQuote,
    'strong': Strong,
    'table': Table,
    'tbody': TableBody,
    'thead': TableHead,
    'text': Text,
    'td': TableData,
    'tr': TableRow,
    'typographic_sym': TypographicSymbol,
    'ul': UnorderedList
}

#--------------------------------------------------------------------------------

def patchFigures(text, slug):
    '''Replace Jekyll figure inclusions with references to PDF figures.'''

    figurePat = re.compile(r'{%\s+include\s+figure.html\s+(.+?)%}', flags=re.DOTALL)
    keyPat = re.compile(r'key="(.+?)"', flags=re.DOTALL)
    captionPat = re.compile(r'caption="(.+?)"', flags=re.DOTALL)
    explainPat = re.compile(r'explain="(.+?)"', flags=re.DOTALL)

    def sub(match):
        body = match.group(1)
        try:
            key = keyPat.search(body).group(1)
            caption = captionPat.search(body).group(1)
            explain = explainPat.search(body).group(1)
            return f'\\figpdf{{{slug}/figures/{key}.pdf}}{{{caption}}}{{f:{slug}:{key}}}'
        except AttributeError as e:
            print(f'figure match failed: {match.group(1)}', file=sys.stderr)
            raise e

    return figurePat.sub(sub, text)


def patchPercentSign(text, slug):
    '''Escape percent signs so that LaTeX doesn't think they're comments.'''
    return text.replace('%', r'{\percent}')


PATCHES = [
    patchFigures,
    patchPercentSign
]

#--------------------------------------------------------------------------------

def extractRaw(text):
    '''Replace content of Jekyll 'raw' commands with random-ish strings.'''

    pat = re.compile(r'{%\s+raw\s+%}(.+?){%\s+endraw\s+%}', flags=re.DOTALL)
    prefix = ''.join([random.choice(string.ascii_lowercase) for i in range(32)])
    inclusions = {}

    def sub(match):
        inclusionId = f'{prefix}={len(inclusions)}'
        inclusions[inclusionId] = match.group(1)
        return inclusionId

    text = pat.sub(sub, text)
    return text, inclusions


def restoreRaw(text, originals):
    '''Re-insert content of Jekyll 'raw' commands.'''

    for (key, value) in originals.items():
        text = text.replace(key, value)
    return text

#--------------------------------------------------------------------------------

def getBody(doc):
    '''Drop the YAML header from the parsed body of the page.'''

    HEADER_TYPES = ['hr', 'p', 'blank']
    HEADER_LEN = len(HEADER_TYPES)
    types = [node['type'] for node in doc['children'][:HEADER_LEN]]
    assert types == HEADER_TYPES, \
        'Did not see Markdown header followed by blank line'
    body = doc['children'][len(HEADER_TYPES):]
    return {'type': '_root', 'children': body}


def parseArgs():
    '''Parse command-line arguments.'''

    parser = argparse.ArgumentParser()
    parser.add_argument('--title', type=str, help='title')
    parser.add_argument('--author', type=str, help='author')
    parser.add_argument('--date', type=str, help='date')
    parser.add_argument('--links', type=str, help='file containing links table')
    parser.add_argument('--glossary', type=str, help='file containing glossary')
    parser.add_argument('--lessons', type=str, help='file containing lesson YAML')
    parser.add_argument('--standards', type=str, help='file containing standards YAML')
    parser.add_argument('--extras', type=str, help='file containing extras YAML')
    parser.add_argument('--template', type=str, help='LaTeX template')
    parser.add_argument('--verbose', action='store_true', help='report progress')
    parser.add_argument('files', type=str, nargs='*')
    return parser.parse_args()


def buildFilenames(args):
    '''
    Build filenames from YAML data.  The three YAML files have slightly
    different keys and values.
    '''

    # Lessons.
    with open(args.lessons, 'r') as reader:
        lessons = yaml.load(reader, Loader=yaml.FullLoader)
        lessons = [{'slug': x['link'].strip('/'),
                    'path': f"{x['link'].strip('/')}/index.md",
                    'title': x['name'],
                    'lede': x['lede']}
                   for x in lessons]

    # Standard files.
    with open(args.standards, 'r') as reader:
        standards = yaml.load(reader, Loader=yaml.FullLoader)
        standards = [{'slug': x['link'].strip('/'),
                      'path': x['path'],
                      'title': x['name']}
                     for x in standards if 'path' in x]

    # Extra files (if present).
    extras = []
    if os.path.isfile(args.extras):
        with open(args.extras, 'r') as reader:
            extras = yaml.load(reader, Loader=yaml.FullLoader)
            extras = [{'slug':x['link'].strip('/'),
                       'path': f"extras/{x['link'].strip('/')}.md",
                       'title': x['name']}
                      for x in extras]

    return {'lessons': lessons, 'standards': standards, 'extras': extras}


def getLinks(filename):
    '''
    Get links from YAML. Returns both the YAML data and Markdown text.
    '''

    with open(filename, 'r') as reader:
        data = yaml.load(reader, Loader=yaml.FullLoader)
    text = [f'[{entry["slug"]}]: {entry["link"]}' for entry in data]
    return data, '\n'.join(text)


def getGlossary(filename):
    '''
    Get glossary from YAML. Returns both the YAML data and Markdown text.
    '''

    with open(filename, 'r') as reader:
        data = yaml.load(reader, Loader=yaml.FullLoader)
    text = [f'[{entry["slug"]}]: ../glossary/#{entry["slug"]}' for entry in data]
    return data, '\n'.join(text)


def lessonsToTopics(lessons):
    '''Convert lessons YAML to Markdown text for inclusion.'''
    rows = '\n'.join([f'| {entry["title"]} | {entry["lede"]} |' for entry in lessons])
    return '\n'.join([
        '| Lesson | Subject |',
        '| ------ | ------- |',
        rows
    ])


def fillInclusions(text, links, topics):
    '''Replace the Jekyll links.md and topics.md inclusions.'''

    text = re.sub(r'{%\s+include\s+links.md\s+%}', links, text)
    text = re.sub(r'{%\s+include\s+topics.html\s+%}', topics, text)
    return text


def glossToMd(glossData):
    '''Convert glossary data to Markdown.'''

    def create(item):
        key = f'g:{item["slug"]}'
        term = item["term"]
        body = item["defn"]
        acronym = f' ({item["acronym"]})' if ("acronym" in item) else ''
        linkStart = f'<a href="{item["link"]}">' if ("link" in item) else ''
        linkEnd = f'</a>' if ("link" in item) else ''
        return f'<dt id="{key}" markdown="1">{linkStart}{term}{linkEnd}{acronym}</dt>' + \
            f'<dd markdown="1">\n{body}\n</dd>'

    lines = ['---',
             "permalink: '/glossary/'",
             '---',
             '',
             '',
             '<dl>'] + \
             [create(item) for item in glossData] + \
             ['</dl>',
              '',
              '{% include links.md %}']
    return '\n'.join(lines)


def linksToMd(linksData):
    '''Convert links data to Markdown.'''

    def create(item):
        slug = item['slug']
        link = item['link']
        name = item['name']
        lede = item['lede']
        return f'<dt id="{slug}" markdown="1">{name}</dt>' + \
            f'<dd markdown="1">\n{lede}\n*<{link}>*\n</dd>'

    lines = ['---',
             "permalink: '/links/'",
             '---',
             '',
             '',
             '<dl>'] + \
             [create(item) for item in linksData] + \
             ['</dl>']
    return '\n'.join(lines)


def swapHandlers(newHandlers):
    '''Replace handlers by key, returning dict of old handlers.'''
    restore = {}
    for key in newHandlers:
        restore[key] = HANDLERS[key]
        HANDLERS[key] = newHandlers[key]
    return restore


def translate(item, links, topics, verbose):
    '''
    Convert all chapters to LaTeX.
    This reads Markdown from a file or uses Markdown provides in the list entry
    (which is done for glossary and links).
    Relies on an external script for parsing to ensure consistency with GitHub.
    If 'handlers' key is present, swap those handlers temporarily.
    '''

    if verbose:
        print(item['slug'], file=sys.stderr)

    title = item['title']
    slug = item['slug']
    if 'markdown' in item:
        markdown = item['markdown']
    elif 'path' in item:
        markdown = open(item['path'], 'r').read()
    else:
        print(f'MISSING markdown AND path in {item}', file=sys.stderr)
        sys.exit(1)

    expanded = fillInclusions(markdown, links, topics)
    raw = bytes(expanded, 'utf-8')
    text = subprocess.run([PARSER], stdout=subprocess.PIPE, input=raw).stdout
    doc = json.loads(text)
    body = getBody(doc)

    writer = io.StringIO()
    writer.write(f'\\chapter{{{title}}}\\label{{s:{slug}}}\n')
    restoreHandlers = None
    if 'handlers' in item:
        restoreHandlers = swapHandlers(item['handlers'])
    Root(body, slug, writer)
    if restoreHandlers:
        swapHandlers(restoreHandlers)

    text = writer.getvalue()
    text, rawInclusions = extractRaw(text)
    print('RAW', rawInclusions, file=sys.stderr)
    for patch in PATCHES:
        text = patch(text, slug)
    text = restoreRaw(text, rawInclusions)

    return text


def main():
    args = parseArgs()
    linksData, linksText = getLinks(args.links)
    glossData, glossText = getGlossary(args.glossary)
    allLinks = linksText + glossText

    content = buildFilenames(args)
    content.update({
        'intro': [{
            'title': 'Introduction',
            'slug': 'intro',
            'path': 'index.md'
        }],
        'glossary': [{
            'title': 'Glossary',
            'slug': 'glossary',
            'markdown': glossToMd(glossData),
            'handlers': {'dt': DefinitionTermGlossary}
        }],
        'links': [{
            'title': 'Links',
            'slug': 'links',
            'markdown': linksToMd(linksData)
        }]
    })

    topics = lessonsToTopics(content['lessons'])
    for key in content:
        content[key] = '\n'.join([translate(item, allLinks, topics, args.verbose)
                                  for item in content[key]])

    content.update({
        'title': args.title,
        'author': args.author,
        'date': args.date
    })
    with open(args.template, 'r') as reader:
        doc = reader.read().format(**content)
        print(doc)


if __name__ == '__main__':
    main()
