# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
import sphinx_wagtail_theme

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath('..'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Orange County Lettings'
copyright = '2025, Dimitri Gaggioli'
author = 'Dimitri Gaggioli'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.coverage',
    'sphinx.ext.napoleon',
    'myst_parser'
]

html_baseurl = "https://oc-lettings-x670.onrender.com/"
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
html_static_path = ['_static']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

extensions.append("sphinx_wagtail_theme")
html_theme = 'sphinx_wagtail_theme'
html_theme_path = [sphinx_wagtail_theme.get_html_theme_path()]
html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "/")
html_js_files = [
    ("readthedocs.js", {"defer": "defer"}),
]

# This is used by Sphinx in many places, such as page title tags.
project = "Orange County Lettings"

# These are options specifically for the Wagtail Theme.
html_theme_options = dict(
    project_name = "Orange County Lettings",
    logo = "img/logo.png",
    logo_alt = "Orange County Lettings",
    logo_height = 70,
    logo_url = "/",
    logo_width = 70,
)

html_theme_options = dict(
    github_url = "https://github.com/dim-gggl/oc_lettings/docs"
)

html_theme_options = dict(
    header_links = "Top 1|http://example.com/one, Top 2|http://example.com/two",
    footer_links = ",".join([
        "On GitHub|https://github.com/dim-gggl/oc_lettings/",
        "The Author|https://github.com/dim-gggl/",
        "OC Lettings Site|https://oc-lettings-x670.onrender.com/",
        "The Docker Image|https://hub.docker.com/repository/docker/dgggl88/oc_lettings/general/",
        "Documentation Theme|https://wagtail.org/",
    ]),
 )