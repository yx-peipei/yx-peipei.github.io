#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from os import getenv

AUTHOR = 'peipei'
SITENAME = "佩佩的小窝"

SITEURL = '//' + getenv("SITEURL", default='localhost:8000')

SITEURL = 'https://yx-peipei.github.io'

OUTPUT_PATH = 'output/'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'zh'

LOCALE = 'zh_CN.UTF-8'

DATE_FORMATS = {
    'zh': ((u'en_US', 'utf8'), u'%a, %d %b %Y',),
}


#DISQUS_SITENAME = 'peipeisblog'
DISQUS_DISPLAY_COUNTS = True
GOOGLE_ANALYTICS = 'UA-163475673-1'


STATIC_PATHS= ['images',
               'pages',
               'static'
               'images/favicon.ico',
               'static/CNAME']

EXTRA_PATH_METADATA = {
    'images/favicon.ico': {'path': 'favicon.ico'},
    'static/CNAME': {'path': 'CNAME'},
    'static/robots.txt': {'path': 'robots.txt'},
    'static/manifest.json': {'path': 'manifest.json'},
#~ 'tag/images': {'path': '../images'}
}

FEED_DOMAIN = SITEURL
FEED_ALL_RSS = 'feed.xml'
FEED_MAX_ITEMS = 9
TAG_FEED_ATOM = None
FEED_ATOM = None
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None

DEFAULT_PAGINATION = 7

ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = PAGE_URL
CATEGORY_URL = '{slug}/index.html'
CATEGORY_SAVE_AS = CATEGORY_URL
TAG_URL = 'tag/{slug}.html'
TAG_SAVE_AS = TAG_URL
TAGS_SAVE_AS = 'tag/index.html'

# -------theme settings, see https://github.com/DandyDev/pelican-bootstrap3/wiki/Variables
THEME = "pelican-themes/pelican-bootstrap3"
BOOTSTRAP_THEME = 'min'
#THEME = "theme"
DISPLAY_TAGS_INLINE = True
DISPLAY_ARTICLE_INFO_ON_INDEX = True
#~ SHOW_ARTICLE_CATEGORY = True

SHOW_SERIES = True
DISPLAY_SERIES_ON_SIDEBAR = True
SERIES_TEXT = 'Part %(index)s of the %(name)s series'

TYPOGRIFY = False
PYGMENTS_STYLE = 'monokai'
GITHUB_USER = 'yx-peipei'
GITHUB_SHOW_USER_LINK = True
GITHUB_REPO = 'yx-peipei/yx-peipei.github.io'

DISPLAY_BREADCRUMBS = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = True

CC_LICENSE = "CC-BY-NC-SA"
OUTPUT_SOURCES = False

DIRECT_TEMPLATES = (('search', 'index', 'categories', 'authors', 'archives','tags'))
AVATAR = 'images/peipei.jpeg'
ABOUT_PAGE = "about.html"


# ------- end theme settings -------


# ------- plugin settings ----------
PLUGIN_PATHS = ['pelican-plugins']

MD_EXTENSIONS = ['admonition',
                 'toc',
                 'codehilite(css_class=highlight,linenums=False)',
                 'extra']



PLUGINS = [#"i18n_subsites",
           "better_codeblock_line_numbering",
           #~ 'better_figures_and_images',
           'tipue_search',
           'neighbors',
           'series',
           'bootstrapify',
           "render_math",
           'extract_toc',
           'tag_cloud',
           'sitemap',
           'summary']

SITEMAP = {
    'format': 'xml',
}

USE_LESS = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = False
#CHECK_MODIFIED_METHOD = "md5"
#LOAD_CONTENT_CACHE = True
#CACHE_CONTENT = True
