import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent))
from pelicanconf import *

SITEURL = "https://www.kemppo.com"
RELATIVE_URLS = False

DELETE_OUTPUT_DIRECTORY = True
