---
permalink: "/glossary/"
---

{% assign current = nil %}
{% for entry in site.data.glossary %}
  {% assign letter = entry.term | remove: "*" | slice: 0, 1 | upcase %}
  {% if letter != current %}
    {% if current != nil %}</dl>{% endif %}
    {% assign current = letter %}
<h2 id="{{letter}}">{{letter}}</h2>
<dl>
  {% endif %}
<dt id="{{entry.slug}}" markdown="1">
  {% if entry.link %}<a href="{{entry.link}}">{% endif %}{{entry.term}}{% if entry.link %}</a>{% endif %}
  {% if entry.acronym %}({{entry.acronym}}){% endif %}
</dt>
<dd markdown="1">
{{entry.defn}}
</dd>
{% endfor %}
</dl>

{% include links.md %}
