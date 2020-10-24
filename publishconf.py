#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
from dotenv import load_dotenv, find_dotenv

sys.path.append(os.curdir)
from pelicanconf import *

dotenv_path = find_dotenv()

# load up the entries as environment variables
load_dotenv(dotenv_path)

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = 'https://www.kemppo.com'
RELATIVE_URLS = True

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

DISQUS_SITENAME = "kemppo-com"
GOOGLE_ANALYTICS = os.environ.get("GOOGLE_ANALYTICS")