#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Colin McLear'
SITENAME = u'Arguments & Argumentation'
SITEURL = 'http://argument.colinmclear.net'
TIMEZONE = 'America/New_York'
DEFAULT_LANG = u'en'
PATH = 'content'
FAVICON = 'images/favicon.ico'
READERS = {'html': None}

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# CACHE SETTINGS ########
# CACHE_CONTENT = True
# CACHE_PATH = '/Users/Roambot/Dropbox/Personal/bin/phil101/cache'
# AUTORELOAD_IGNORE_CACHE = True
# LOAD_CONTENT_CACHE = True
# CHECK_MODIFIED_METHOD = 'mtime'


# THEME SETTINGS ########
THEME = 'pelican-bootstrap3'
BOOTSTRAP_THEME='simplex'
BOOTSTRAP_NAVBAR_INVERSE = True
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_ARTICLE_INFO_ON_INDEX = True
DISPLAY_PAGES_ON_MENU = False
NEWEST_FIRST_ARCHIVES = False
MENUITEMS = (
    ('Texts', '/texts'),
    ('Excercises & Assignments', '/excercises'),
    ('Resources', '/resources'),
    ('Contact', '/contact'),
    # ('Tags', '/tags.html'),
    # ('Home', '/'),
    # ('Category1', 'category/category1.html'),
    # ('Category2', 'category/category2.html'),
)
THEME_STATIC_DIR = 'theme'
# Turn on Typogrify
TYPOGRIFY = True
CC_LICENSE = "CC-BY-NC-SA"
ARTICLE_PATHS = ['texts']
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'
INDEX_SAVE_AS = 'texts/index.html'
INDEX_URL = 'texts/'
CUSTOM_CSS = 'static/custom.css'
STATIC_PATHS = ['images', 'pdfs', 'extra']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, 'extra/custom.css': {'path': 'static/custom.css'}}
DIRECT_TEMPLATES = ('index', 'tags', 'authors', 'archives', 'search')

# Plugins ##########
PLUGIN_PATHS = ['/Users/roambot/bin/pelican-plugins']
PLUGINS = ['pandoc_reader', 'assets', 'tipue_search', 'tag_cloud', 'neighbors', 'extract_toc']

PANDOC_ARGS = [
    '--filter=/usr/local/bin/pandoc-citeproc',
    '--base-header-level=2',
    '--bibliography=/Users/roambot/Dropbox/Work/master.bib',
    '--toc',
    '--toc-depth=5',
  ]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Tags

TAG_CLOUD = True
DISPLAY_TAGS_ON_SIDEBAR= True
DISPLAY_TAGS_INLINE = True
TAG_CLOUD_STEPS = 5
TAG_CLOUD_MAX_ITEMS = 100
# TAG_CLOUD_SORTING = 'random'


# Blogroll
LINKS = (
        ('A link', 'http://'),
    )

DEFAULT_PAGINATION = 10

