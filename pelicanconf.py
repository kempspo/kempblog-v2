#!/usr/bin/env python
from datetime import datetime

AUTHOR = "Kemp Po"
SITEURL = ""
SITENAME = "Kemp Po"
SITETITLE = "Kemp Po"
SUBTITLE = "Kemp Po's Thoughts and Writings"
SITELOGO = SITEURL + "/images/profile.png"
# FAVICON = SITEURL + "/images/favicon.ico"

PATH = "content"

TIMEZONE = "Asia/Manila"
DATE_FORMATS = {
    "en": "%B %d, %Y",
}

DEFAULT_LANG = "en"

STATIC_PATHS = ["images"]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (("github", "https://github.com/kempspo"),
#          ("linkedin", "https://www.linkedin.com/in/kemp-po/"),
#         #  ("Jinja2", "http://jinja.pocoo.org/"),)

# Social widget
SOCIAL = (("github", "https://github.com/kempspo"),
          ("linkedin", "https://www.linkedin.com/in/kemp-po/"))

BROWSER_COLOR = "#333"
ROBOTS = "index, follow"

PATH = "content"
OUTPUT_PATH = "blog/"

PLUGIN_PATHS = ["C:/Users/Kemp/Desktop/JupyterDump/pelican-plugins"]
PLUGINS = ["i18n_subsites"]

THEME = "C:/Users/Kemp/Desktop/JupyterDump/Flex"
THEME_COLOR = "dark"
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

PYGMENTS_STYLE = "emacs"
PYGMENTS_STYLE_DARK = "monokai"

COPYRIGHT_YEAR = datetime.now().year

DEFAULT_PAGINATION = 10

USE_FOLDER_AS_CATEGORY = False

MAIN_MENU = True
MENUITEMS = (
    ("Blog", "/category/blog.html"),
    ("Notes", "/category/notes.html"),
)

USE_LESS = True
