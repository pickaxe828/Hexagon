import sys

class token:
    TOKEN = "NzEzMDY0ODcwOTI0MjU1MjYz.XsaraQ.dESXFtmf4ew-bEAD_LrHWljzKEQ"
    debug_TOKEN = "NzgxODkxMjA1OTgyMDYwNTg0.X8EO7g.phSaF-cW2zV674lmiXOKDYsIWQY"

    youtube_TOKEN = "AIzaSyDMJdWCdhw4tN4ecuj94krrXA_JvwLmX-Y"

def prefix():
    if '--debug' in sys.argv:
        return "/"
    else:
        return "."
