#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://yx-peipei.github.io'
GITHUB_URL = 'https://github.com/yx-peipei'

OUTPUT_PATH = '../'
RELATIVE_URLS = False
FEED_DOMAIN = SITEURL
DELETE_OUTPUT_DIRECTORY = False

USE_LESS = False

# Following items are often useful when publishing



#DISQUS_SITENAME = 'xweisblog'
#DISQUS_DISPLAY_COUNTS = False
#GOOGLE_ANALYTICS = 'UA-30756331-1'

TAG_FEED_ATOM = 'feeds/tag-%s.atom.xml'
FEED_ALL_ATOM = 'feeds/all.atom.xml'
#FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ATOM = 'feeds/atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

LOAD_CONTENT_CACHE = False
