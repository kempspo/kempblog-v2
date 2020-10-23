from datetime import datetime

AUTHOR = "Kemp Po"
SITEURL = ""
SITENAME = "Kemp Po"
SITETITLE = "Kemp Po"
SITESUBTITLE = "Thoughts of a data person"
SITELOGO = SITEURL + "/images/profile.jpg"
FAVICON = SITEURL + "/images/favicon.ico"
BROWSER_COLOR = "#333333"
PYGMENTS_STYLE = "paraiso-light"
PYGMENTS_STYLE_DARK = "paraiso-dark"

ROBOTS = "index, follow"

THEME = "theme/"
THEME_COLOR = "dark"
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True
PATH = "content"
OUTPUT_PATH = "output/"

TIMEZONE = "Asia/Manila"
DATE_FORMATS = {
    "en": "%B %d, %Y",
}

COPYRIGHT_YEAR = datetime.now().year
COPYRIGHT_NAME = "Kemp Po"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll

# Social widget
SOCIAL = (("github", "https://github.com/kempspo"),
          ("linkedin", "https://www.linkedin.com/in/kemp-po/"))

PLUGIN_PATHS = ["C:/Users/Kemp/Desktop/JupyterDump/pelican-plugins"]
PLUGINS = ["i18n_subsites"]

CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike",
    "version": "4.0",
    "slug": "by-sa",
}

DEFAULT_PAGINATION = 10

USE_FOLDER_AS_CATEGORY = False

MAIN_MENU = True
MENUITEMS = (
    ("Archives", "/archives.html"),
    ("Category", "/categories.html"),
)

USE_LESS = True

STATIC_PATHS = ["images", "extra/ads.txt", "extra/CNAME"]

EXTRA_PATH_METADATA = {
    "extra/ads.txt": {"path": "ads.txt"},
    "extra/CNAME": {"path": "CNAME"},
}