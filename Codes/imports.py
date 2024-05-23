# imports.py

import os
from itertools import compress as compress
import re
import datetime as dt
import pytz
import getGlobalVariables
from logError import logErrorProgram as logErrorProgram
from checkFolderStructure import checkFolderStructure as checkFolderStructure
from statistics import median as median
from ffmpy import FFmpeg as FFmpeg
from fileLoopFFMPEGconverterCompressor import fileLoopFFMPEGconverterCompressor as fileLoopFFMPEGconverterCompressor
from videoConvertorCompressor import videoConvertorCompressor as videoConvertorCompressor

__all__ = [
    'os',
    'compress',
    're',
    'dt',
    'pytz',
    'getGlobalVariables',
    'logErrorProgram',
    'checkFolderStructure',
    'median',
    'FFmpeg',
    'fileLoopFFMPEGconverterCompressor',
    'videoConvertorCompressor'
]

print("Imported {0} libraries to run {1}: {2}".format(len(__all__),videoConvertorCompressor.__name__,__all__))