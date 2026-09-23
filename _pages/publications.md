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

Below is a selection of publications I co-authored. See my [Google Scholar profile](https://scholar.google.com/citations?user=d1hglOMAAAAJ) and [RMA research profile](https://researchportal.rma.ac.be/en/persons/maxim-vochten/) for a fuller record.

### Recent work at RMA

- T.-T. Nguyen, M. Vochten, G. De Cubber, B. Janssens and H. Bruyninckx, “[Predictive and Inertia-Aware Motion Planning for USV Navigation in Cluttered Harbors](https://researchportal.rma.ac.be/en/publications/predictive-and-inertia-aware-motion-planning-for-usv-navigation-i/),” IFAC World Congress, 2026.
- T. T. Nguyen, M. Vochten, H. Chaudhary and G. De Cubber, “[Deep Long-Term Ship Motion Prediction with Anomaly Detection for Autonomous Maritime UAV Landing](https://doi.org/10.1007/978-3-032-29469-2_27),” *Robotics and Mechatronics: Proceedings of ISRM 2026*, 2026.
- V. Jardim Bueno and M. Vochten, “[Shared Autonomy for Robotic Manipulation in Explosive Ordnance Disposal: Insights from the GENIUS Project](https://researchportal.rma.ac.be/en/publications/shared-autonomy-for-robotic-manipulation-in-explosive-ordnance-di/),” extended abstract presented at ICRA 2026.

### Earlier selected publications

<div class="publications">

{%- for section in page.sections %}
  <a id="{{section.text}}"></a>
  <p class="bibtitle">{{section.text}}</p>

  {% bibliography -f {{site.scholar.bibliography}} -q {{section.bibquery}} %}

{%- endfor %}

</div>
