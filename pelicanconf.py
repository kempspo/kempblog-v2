from datetime import datetime

AUTHOR = "Kemp Po"
SITENAME = "Kemp Po"
SITEURL = ""

PATH = "content"
OUTPUT_PATH = "output"
TIMEZONE = "Asia/Manila"
DEFAULT_LANG = "en"
DATE_FORMATS = {
    "en": "%B %-d, %Y",
}

THEME = "theme"
RELATIVE_URLS = True

ARTICLE_URL = "{slug}.html"
ARTICLE_SAVE_AS = "{slug}.html"
PAGE_URL = "{slug}.html"
PAGE_SAVE_AS = "{slug}.html"

DIRECT_TEMPLATES = ["index", "writing", "sitemap", "robots"]
SITEMAP_SAVE_AS = "sitemap.xml"
ROBOTS_SAVE_AS = "robots.txt"
ARCHIVES_SAVE_AS = ""
YEAR_ARCHIVE_SAVE_AS = ""
MONTH_ARCHIVE_SAVE_AS = ""
DAY_ARCHIVE_SAVE_AS = ""
AUTHORS_SAVE_AS = ""
CATEGORIES_SAVE_AS = ""
TAGS_SAVE_AS = ""
AUTHOR_SAVE_AS = ""
CATEGORY_SAVE_AS = ""
TAG_SAVE_AS = ""

DEFAULT_PAGINATION = False
USE_FOLDER_AS_CATEGORY = False

FEED_DOMAIN = "https://www.kemppo.com"
FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
    },
    "output_format": "html5",
}

STATIC_PATHS = ["images"]

COPYRIGHT_YEAR = datetime.now().year
COPYRIGHT_NAME = "Kemp Po"
CC_LICENSE_URL = "https://creativecommons.org/licenses/by-sa/4.0/"
