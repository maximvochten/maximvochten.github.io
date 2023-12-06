---
layout: page
permalink: /publications/
title: Publications
description: A selected list of publications I authored.
sections:
  - bibquery: "@article[doi]"
    text: "Journal articles"
  - bibquery: "@inproceedings[doi]"
    text: "Conference papers"
  - bibquery: "@inproceedings[comment=workshop]"
    text: "Workshop papers and dissemination"
  - bibquery: "@phdthesis"
    text: "Thesis"
nav: true
nav_order: 1
---

See my [Google Scholar profile](https://scholar.google.be/citations?user=d1hglOMAAAAJ&hl=en]) for a more complete overview.

<div class="publications">

{%- for section in page.sections %}
  <a id="{{section.text}}"></a>
  <p class="bibtitle">{{section.text}}</p>

  {% bibliography -f {{site.scholar.bibliography}} -q {{section.bibquery}} %}

{%- endfor %}

</div>
