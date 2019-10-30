# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

## import pytorch_sphinx_theme
## import sphinx_theme
import edx_theme

sys.path.insert(0, os.path.abspath("../.."))

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.autosummary',
    'sphinx.ext.coverage',
    'sphinx.ext.doctest',
    'sphinx.ext.githubpages',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx_theme'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

pygments_style = 'sphinx'

# -- Project information -----------------------------------------------------

project = 'torecsys'
copyright = '2019, Jasper, Li Wai Yin'
author = 'Jasper, Li Wai Yin'

# The full version, including alpha/beta/rc tags
version = "dev-0.0.1"
release = "dev"

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# Disable docstring inheritance
autodoc_inherit_docstrings = True

# autosectionlabel throws warnings if section names are duplicated.
# The following tells autosectionlabel to not throw a warning for
# duplicated section names that are in different documents.
autosectionlabel_prefix_document = True

# Configuration of sphinx 
add_function_parentheses = False
add_module_names = False
autoclass_content = "both"
autodoc_mock_imports = ["torch", "torchaudio", "torchvision", "torchtext"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
## html_theme = 'neo_rtd_theme'
## html_theme_path = [sphinx_theme.get_html_theme_path('neo_rtd_theme')]
html_theme = 'edx_theme'
html_theme_path = [edx_theme.get_html_theme_path()]
html_favicon = os.path.join(html_theme_path[0], 'edx_theme', 'static', 'css', 'favicon.ico')

html_theme_options = {
    ## 'canonical_url': 'https://torecsys.readthedocs.io/en/latest/',
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_title = "Torecsys Documentation - Torescys Master Documentation"
html_short_title = "torecsys documentation"
html_baseurl = "https://torecsys.readthedocs.io/"
html_static_path = ['_static']
html_logo = "_static/img/pytorch-logo-dark.svg"
html_favicon = "_static/img/pytorch-logo-flame.svg"
html_sidebars = {
    "**": [
        "index.html", "search.html"
    ]
}

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
intersphinx_mapping = {
    'python': ('https://docs.python.org/', None),
    'numpy': ('https://docs.scipy.org/doc/numpy/', None),
    'pytorch': ('https://pytorch.org/docs/', None)
}
