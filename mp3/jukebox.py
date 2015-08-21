#!/usr/bin/env python

# Jukebox class.
# When initialize, scan a directory for mp3 files.
# This package suppot play stop

import os
import logging
import sys

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


class Jukebox:

    libs=[]
    MUSICS_FOLDER=""

    def __init__(self):
        global libs
        for root, dirs, files in os.walk("/home/junyu/"):
           for file in files:
               if file.endswith("*.mp3"):
                   libs.append(file)
    # used by print function.
    def __str__(self):
        pass


if __name__ == "__main__":
     jukebox = Jukebox()
     print __file__

