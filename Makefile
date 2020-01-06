include _config.mk

LESSONS=$(wildcard */index.md)
STANDARDS=$(filter-out README.md,$(wildcard *.md))
STANDARDS_RELEASE=$(filter-out index.md,$(filter-out references.md,${STANDARDS}))
EXTRAS=$(wildcard extras/*.md)
SOURCE=${LESSONS} ${STANDARDS} ${EXTRAS}

DATA=$(wildcard _data/*.yml)

FIG_SVG=$(wildcard */figures/*.svg)
FIG_PDF=$(patsubst %.svg,%.pdf,${FIG_SVG})

# Controls
all : commands

## commands : show all commands.
commands :
	@grep -h -E '^##' ${MAKEFILE_LIST} | sed -e 's/## //g'

## build    : rebuild site without serving it.
build :
	rm -rf .jekyll-cache .jekyll-metadata _site
	jekyll build

## serve    : rebuild site and serve it.
serve:
	rm -rf _site
	jekyll serve -I

## bib      : regenerate Markdown bibliography from BibTeX.
bib: references.md

references.md: references.bib
	bin/bib2md.py < references.bib > references.md

## book.tex : make LaTeX source.
book.tex: bin/md2tex.py bin/md2ast.rb etc/latex.template ${SOURCE} ${DATA}
	python bin/md2tex.py \
	--title ${TITLE} \
	--author ${AUTHOR} \
	--date ${YEAR}/${VERSION} \
	--links _data/links.yml \
	--glossary _data/glossary.yml \
	--lessons _data/lessons.yml \
	--standards _data/standards.yml \
	--extras _data/extras.yml \
	--template etc/latex.template \
	> book.tex

## book.pdf : make PDF from LaTeX source.
book.pdf: book.tex etc/settings.tex ${FIG_PDF}
	pdflatex --shell-escape book.tex
	biber book
	makeindex book
	pdflatex --shell-escape book
	pdflatex --shell-escape book

%.pdf : %.svg
	rsvg-convert -f pdf -o $@ $<

## ----------------------------------------

## config   : Regenerate configuration file.
config: bin/makeconfig.py etc/config.template _config.mk
	@bin/makeconfig.py \
	title=${TITLE} \
	subtitle=${SUBTITLE} \
	author=${AUTHOR} \
	year=${YEAR} \
	version=${VERSION} \
	email=${EMAIL} \
	domain=${DOMAIN} \
	repo=${REPO} \
	excludes='${EXCLUDES}' \
	< etc/config.template \
	> _config.yml

## links    : Check that all links resolve.
links:
	bin/checklinks.py _data/links.yml _data/glossary.yml ${SOURCE}

## clean    : Clean up stray files.
clean:
	rm -rf _site
	find . -name '*~' -exec rm {} \;
	rm -f book.*

## sterile  : Clean up everything.
sterile: clean
	rm -rf $$(cat .gitignore) _minted-book

## release  : Create release of template.
release : clean
	@tar zcvf release.tar.gz \
	.gitignore \
	Makefile \
	_data/standards.yml \
	_includes \
	_layouts \
	assets \
	bin \
	etc \
	favicon.ico \
	${STANDARDS_RELEASE}

## settings : Show values of variables.
settings :
	@echo TITLE: ${TITLE}
	@echo YEAR: ${YEAR}
	@echo EMAIL: ${EMAIL}
	@echo DOMAIN: ${DOMAIN}
	@echo REPO: ${REPO}
	@echo EXCLUDES: ${EXCLUDES}
	@echo LESSONS: ${LESSONS}
	@echo STANDARDS: ${STANDARDS}
	@echo EXTRAS: ${EXTRAS}
	@echo SOURCE: ${SOURCE}
