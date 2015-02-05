# DPaW Django web template

This project consists of a basic Django application containing HTML
templates that provide a starting point for web applications used by the
Department. The base template consists of a mobile-friendly HTML5
template with a fixed top navbar containing the DPaW logo, plus static
assets. The project also contains functional examples of **login** and
**logged out** templates.

The base template is based upon [HTML5 Boilerplate](https://html5boilerplate.com/)
styled with [Bootstrap 3](https://getbootstrap.com/), with some
additional styling via the [Bootflat UI
kit](https://bootflat.github.io/).

## Installation and usage

1. Clone the repository.
2. Copy the *webtemplate_dpaw* directory into your own project.
3. Extend the base template by placing the following at the head of your
   own templates: `{% extends "webtemplate_dpaw/base.html" %}`
4. Place page content within the required blocks.

The main template blocks are as follows:

* `navbar_links`
* `page_content`
* `page_footer`
