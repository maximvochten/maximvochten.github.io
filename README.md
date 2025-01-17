# Installation

**Do not try to install locally on Windows**. Multiple problems: imagemagick error, .exe file permissions (jupyter), rubygems in wrong location, etc...

Instead use Docker. 

# Locally testing website

Open Terminal:
- start http://localhost:8080/
- docker compose pull
- docker compose up

Or run `windows_test_local.sh`

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

# Old about page

	I am a Postdoctoral Research Associate within the [Robotics Research Group](https://www.mech.kuleuven.be/en/pma/research/robotics) at [KU Leuven](https://www.kuleuven.be). 

	My main aim in research is to improve the collaboration between humans and robots by formulating data-efficient task representations that can be used for human intent recognition and for the fast programming of reactive robot motions. To achieve this, I combine concepts from numerical optimization, optimal control, differential geometry, screw theory, 3D kinematics, state estimation and robot control.

	I am currently working on the [Robotgenskill project](https://robotgenskill.pages.gitlab.kuleuven.be/) which focuses on the generalization of human-demonstrated robot skills.

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

