import os

from alphahunt_sdk._version import __version__

VERSION = __version__

TOKEN = os.getenv("ALPHAHUNT_TOKEN")
REMOTE = os.getenv("ALPHAHUNT_REMOTE", "https://api.alphahunt.io")
API_VERSION = os.getenv("ALPHAHUNT_API_VERSION", "4")

HEADERS = {
    "User-Agent": f"alphahuntsdk-py/{VERSION}",
    "Accept": f"application/vnd.alphahunt.v{API_VERSION}+json",
    "Content-Type": "application/json",
}

RETRIES = int(os.getenv("ALPHAHUNTSDK_RETRIES", 5))
RETRIES_BACKOFF = int(os.getenv("ALPHAHUNTSDK_RETRIES_BACKOFF", 0.1))
