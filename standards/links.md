---
permalink: "/links/"
---

<table>
<tr><th>Site</th><th>Description</th></tr>
{% for entry in site.data.links %}
<tr>
  <td><a href="{{entry.link}}">{{entry.name | markdownify | replace: '<p>', '' | replace: '</p>', ''}}</a></td>
  <td>{{entry.lede | markdownify | replace: '<p>', '' | replace: '</p>', ''}}</td>
</tr>
{% endfor %}
</table>

{% include links.md %}
