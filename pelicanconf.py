#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Tobias Brandt'
SITENAME = u'centiBils'
SITESUBTITLE = 'logreturns for humans'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Africa/Johannesburg'

DEFAULT_LANG = u'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Menu
MENUITEMS = (('Intro', 'pages/intro.html'),
             ('Uses', 'pages/uses.html'),
             ('About', 'pages/about.html'),)

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#THEME = "C:\\Users\\Tobias\\Documents\\Python Scripts\\pelican-themes\\bootlex"
#THEME = '../pelican-themes/pelican-blue'
THEME = '../flask-pelican-theme'

# Plugins
PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.vimeo',
           'liquid_tags.include_code', 'liquid_tags.notebook']
NOTBOOK_DIR = 'notebooks'
EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')
