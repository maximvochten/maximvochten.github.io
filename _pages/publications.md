---
layout: page
permalink: /publications/
title: Publications
description: 
sections:
  - bibquery: "@article[doi,bibtex_show=true]"
    text: "Journal articles"
  - bibquery: "@inproceedings[doi,bibtex_show=true]"
    text: "Conference papers"
  - bibquery: "@inproceedings[comment=workshop,bibtex_show=true]"
    text: "Workshop papers and dissemination"
  - bibquery: "@phdthesis"
    text: "Thesis"
nav: true
nav_order: 1
---

Below you can find a selected list of publications I (co-)authored. Please visit my [Google Scholar profile](https://scholar.google.be/citations?user=d1hglOMAAAAJ&hl=en]) for a more complete overview.

<div class="publications">

{%- for section in page.sections %}
  <a id="{{section.text}}"></a>
  <p class="bibtitle">{{section.text}}</p>

  {% bibliography -f {{site.scholar.bibliography}} -q {{section.bibquery}} %}

{%- endfor %}

</div>
