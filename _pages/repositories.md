---
layout: page
permalink: /repositories/
title: Software
description: Selection of developed software
nav: false
nav_order: 3
published: false
---



## Software repositories

{% if site.data.repositories.github_repos %}
<div class="repositories d-flex flex-wrap flex-md-row flex-column justify-content-between align-items-center">
  {% for repo in site.data.repositories.github_repos %}
    {% include repository/repo.liquid repository=repo %}
  {% endfor %}
</div>
{% endif %}
