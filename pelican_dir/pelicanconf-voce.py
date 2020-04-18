#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals
from datetime import date
import time
import os

AUTHOR = 'peipei'
SITENAME = '佩佩的小窝'
SITEURL = 'http://yx-peipei.github.io'
USER_LOGO_URL = 'images/peipei.jpeg'
#INDEX_TITLE = 'Site Title'
#INDEX_DESC = ''

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'zh'
DEFAULT_DATE_FORMAT = "%b %d, %Y"
LOCALE = 'zh_CN.UTF-8'

DATE_FORMATS = {
    'zh': ((u'en_US', 'utf8'), u'%a, %d %b %Y',),
}
CURRENT_YEAR = date.today().year
PAGE_GEN_TIME = time.strftime("%c")

THEME = "pelican-themes/voce"

PLUGIN_PATHS = ["pelican-plugins", os.path.join(THEME, "plugins")]
PLUGINS = ["assets", "sitemap"]
MARKDOWN = {
    'extensions' : ['markdown.extensions.codehilite', 'markdown.extensions.extra', 'markdown.extensions.admonition'],
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight','guess_lang': 'False', 'linenums': 'True'},
    },
    'output_format': 'html5',
}

LOAD_CONTENT_CACHE = False
SLUGIFY_SOURCE = 'basename'

READERS = {'html': None}

STATIC_PATHS= ['images',
               'pages',
               'static'
               'images/favicon.ico',
               'static/CNAME']


EXTRA_PATH_METADATA = {
    'images/favicon.ico': {'path': 'favicon.ico'},
    #'images/favicon-16x16.png': {'path': 'favicon-16x16.png'},
    #'images/favicon-32x32.png': {'path': 'favicon-32x32.png'},
    #'images/favicon-96x96.png': {'path': 'favicon-96x96.png'},
    'static/CNAME': {'path': 'CNAME'},
    'static/robots.txt': {'path': 'robots.txt'},
    'static/manifest.json': {'path': 'manifest.json'},
}

#Theme specific
GOOGLE_ANALYTICS_ID = "UA-163475673-1"
GOOGLE_ANALYTICS_PROP = "yx-peipei.github.io"
TAGLINE = "Site Tagline"
DISPLAY_TAGS_INLINE = True
MANGLE_EMAILS = False
GLOBAL_KEYWORDS = ("keywords",)

# Webassets plugin
ASSET_CONFIG = (("url_expire", False),)
ASSET_DEBUG = False

SOCIAL = (
    ("Feed", "http://yx-peipei.github.io/feeds/all.atom.xml"),
    ('Email','mailto:talk2yixuan@gmail.com')
    #("GitHub", "yx-peipei/yx-peipei.github.io"),
)

LINKS = (('Home','/index.html'),  
     ('About Me','about.html'),)

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 1,
        'pages': 0.8
    },
    'changefreqs': {
        'articles': 'never',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

DEFAULT_PAGINATION = 8

RELATIVE_URLS = True
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = [".git"]

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
SUMMARY_MAX_LENGTH = 10

ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = PAGE_URL
CATEGORY_URL = '{slug}/index.html'
CATEGORY_SAVE_AS = CATEGORY_URL
TAG_URL = 'tag/{slug}.html'
TAG_SAVE_AS = TAG_URL
TAGS_SAVE_AS = 'tag/index.html'
