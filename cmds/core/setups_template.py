import sys

class token:
    TOKEN = "hexagon-token"
    debug_TOKEN = "hexagon-canary-token"

    youtube_TOKEN = "google-api-token"

def prefix():
    if '--debug' in sys.argv:
        return "/"
    else:
        return "."
