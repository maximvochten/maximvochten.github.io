# Installation

**Do not** try to install locally on Windows. Multiple problems: imagemagick error, .exe file permissions (jupyter), rubygems in wrong location, etc...

Instead use docker. 

# Custom changes

1. includes/projects_horizontal.liquid : remove text-lowercase from card-title

2. includes/projects.liquid : remove text-lowercase from card-title

3. sass_base.scss : 
/* Bib type style */
p.bibtitle {
	color: var(--global-theme-color);
    	font-weight: 400;
    	font-size: 1.5em;
    	text-align: center;
    	border-bottom: 1px solid #bbb;
}

4. In about.liquid : News | Latest posts | Recent publications 

5. custom layout of cv page: _layouts/cv_maxim.liquid

# Track

Track performance of website using:
- google search console
- google analytics

# Contents

- **_config.yml**: configuratie site
- **assets**: files, videos, images, papers, ...
- **_bibliography**: bib file
- **blog**: index pagina van blog
- **_data**: yml files repo, co-authors, cv, journals 

- **_layouts**: HTML pages met layout van globale pagina's
- **_includes** HTML files voor kleine onderdelen op de pagina's

- **_news**: announcements
- **_pages**: md files met info die in pagina's moet
- **_plugins**: ruby scripts
- **_posts**: blog posts
- **_projects**: project pagina's
- **_site**: gegenereerde site
- **_sass**: css files
- **reports**: svg files

