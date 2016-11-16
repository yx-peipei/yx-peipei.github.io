#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from os import getenv

AUTHOR = 'peipei'
SITENAME = "peipei's blog"

SITEURL = '//' + getenv("SITEURL", default='localhost:8000')

SITEURL = 'http://yx-peipei.github.io'

OUTPUT_PATH = 'output/'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'zh'

LOCALE = 'zh_CN.utf8'

DATE_FORMATS = {
    'zh': ((u'en_US', 'utf8'), u'%a, %d %b %Y',),
}


#DISQUS_SITENAME = 'peipeisblog'
#DISQUS_DISPLAY_COUNTS = False
#GOOGLE_ANALYTICS = 'UA-30756331-1'




TAG_FEED_ATOM = None
FEED_ATOM = None
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None

DEFAULT_PAGINATION = 7

PAGE_URL = "{slug}.html"
PAGE_SAVE_AS = "{slug}.html"
PAGE_PATHS = ['pages']
#~ TAG_SAVE_AS='tag_{slug}.html'
#~ CATEGORY_SAVE_AS='category_{slug}.html'

# -------theme settings, see https://github.com/DandyDev/pelican-bootstrap3/wiki/Variables
THEME = "pelican-themes/pelican-bootstrap3"
DISPLAY_TAGS_INLINE = True
DISPLAY_ARTICLE_INFO_ON_INDEX = True
#~ SHOW_ARTICLE_CATEGORY = True

SHOW_SERIES = True
DISPLAY_SERIES_ON_SIDEBAR = True
SERIES_TEXT = 'Part %(index)s of the %(name)s series'

TYPOGRIFY = False
PYGMENTS_STYLE = 'manni'
GITHUB_USER = 'yx-peipei'
GITHUB_SHOW_USER_LINK = True

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
#RELATIVE_URLS = True
#CHECK_MODIFIED_METHOD = "md5"
#LOAD_CONTENT_CACHE = True
#CACHE_CONTENT = True
