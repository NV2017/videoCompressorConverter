# imports.py

import os
import datetime as dt
import pytz
import getGlobalVariables
from logError import logErrorProgram as logErrorProgram
# from logError import ProgramLogRecord as ProgramLogRecord
from checkFolderStructure import checkFolderStructure as checkFolderStructure
from videoConvertorCompressor import videoConvertorCompressor as videoConvertorCompressor

__all__ = [
    'os',
    'dt',
    'pytz',
    'getGlobalVariables',
    'logErrorProgram',
    'checkFolderStructure',
    'videoConvertorCompressor'
]

print("Imported {0} libraries to run {1}: {2}".format(len(__all__),videoConvertorCompressor.__name__,__all__))