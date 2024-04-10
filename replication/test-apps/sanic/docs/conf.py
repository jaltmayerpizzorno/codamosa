#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Sanic documentation build configuration file, created by
# sphinx-quickstart on Sun Dec 25 18:07:21 2016.
#
# This file is execfile()d with the current directory set to its
# containing dir.

import os
import sys

# Add support for auto-doc
import recommonmark

from recommonmark.transform import AutoStructify


# Ensure that sanic is present in the path, to allow sphinx-apidoc to
# autogenerate documentation from docstrings
root_directory = os.path.dirname(os.getcwd())
sys.path.insert(0, root_directory)

import sanic


# -- General configuration ------------------------------------------------

extensions = ["sphinx.ext.autodoc", "recommonmark"]

templates_path = ["_templates"]

# Enable support for both Restructured Text and Markdown
source_suffix = [".rst", ".md"]

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "Sanic"
copyright = "2021, Sanic Community Organization"
author = "Sanic Community Organization"

html_logo = "./_static/sanic-framework-logo-white-400x97.png"
# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = sanic.__version__
# The full version, including alpha/beta/rc tags.
release = sanic.__version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
#
# modules.rst is generated by sphinx-apidoc but is unused. This suppresses
# a warning about it.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "modules.rst"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_css_files = ["custom.css"]
# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "Sanicdoc"

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,
        "Sanic.tex",
        "Sanic Documentation",
        "Sanic contributors",
        "manual",
    ),
]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "sanic", "Sanic Documentation", [author], 1)]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "Sanic",
        "Sanic Documentation",
        author,
        "Sanic",
        "One line description of project.",
        "Miscellaneous",
    ),
]

# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# A list of files that should not be packed into the epub file.
epub_exclude_files = ["search.html"]

# -- Custom Settings -------------------------------------------------------

suppress_warnings = ["image.nonlocal_uri"]


autodoc_typehints = "description"
autodoc_default_options = {
    "member-order": "groupwise",
}


# app setup hook
def setup(app):
    app.add_config_value(
        "recommonmark_config",
        {
            "enable_eval_rst": True,
            "enable_auto_doc_ref": False,
        },
        True,
    )
    app.add_transform(AutoStructify)


html_theme_options = {
    "style_external_links": False,
}