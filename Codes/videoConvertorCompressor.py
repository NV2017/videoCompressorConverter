# videoConvertorCompressor.py

from imports import *

def videoConvertorCompressor():
    try:
        # Check Input Output folder structure
        checkFolderStructureStatus = checkFolderStructure()
        print("checkFolderStructureStatus:", checkFolderStructureStatus)
    except Exception as videoConvertorCompressorError:
        print("Unable to finish {0}, error: {1}".format(__name__, videoConvertorCompressorError))
    # End of 'try:'
# End of 'def videoConvertorCompressor():'