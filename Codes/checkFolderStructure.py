# checkFolderStructure.py

from imports import *

# Given a path, this function creates folder if absent
# Return True if created or no path input; returns False if unable to create
def ifNotFolderThenCreate(_FolderPath: str = None) -> bool: # Sort of private function, not used elsewhere
    if _FolderPath == None:
        print("No folder path input to create, using {0}".format(__name__))
        return True
    # End of 'if _FolderPath == None:'

    try:
        if not os.path.exists(_FolderPath):
            os.mkdir(_FolderPath)
            print("Created folder path: {0}, using {1}".format(_FolderPath, __name__))
        else:
            print("Detected folder path: {0}, using {1}".format(_FolderPath, __name__))
        # End of 'if not os.path.exists(_FolderPath):'
        return True
    except Exception as ifNotFolderThenCreateError:
        print("Error detecting folder path: {0}, using: {1}. Error: {2}".format(_FolderPath, __name__, ifNotFolderThenCreateError))
        return False
    # End of 'try:'
# End of 'def ifNotFolderThenCreate(_FolderPath):'

# Given a start and an end path, this function will make same folder in end path as in start path
# Returns False when there is no input provided, False when Error, True when task done
def mappingFolderStructure(_mapStartFolderPath: str = None, _mapEndFolderPath: str = None):
    if None in [_mapStartFolderPath, _mapEndFolderPath]:
        return True
    # End of 'if None in [_mapStartFolderPath, _mapEndFolderPath]:'

    try:
        for path, subdirs, files in os.walk(_mapStartFolderPath):
            for subdir in subdirs:
                tempMapStartFolderPath = os.path.join(path, subdir)
                tempEquivalentMapEndFolderPath = tempMapStartFolderPath.replace(_mapStartFolderPath, _mapEndFolderPath)
                tempEquivalentMapEndFolderPathStatus = ifNotFolderThenCreate(_FolderPath = tempEquivalentMapEndFolderPath)
            # End of 'for dir in dir_:'
        # End of 'for dir_, _, files in os.walk(_mapStartFolderPath):'
        return tempEquivalentMapEndFolderPathStatus
    except Exception as mappingFolderStructureError:
        print("Error mapping folders from: {0} to: {1} using {2}. Error: {3}".format(_mapStartFolderPath, _mapEndFolderPath, __name__, mappingFolderStructureError))
        return False
    # End of 'try:'
# End of 'def mappingFolderStructure(_mapStartFolderPath: str = , _mapEndFolderPath: str = ):'

# Not a private function, this function is called in 'videoConverterCompressor'
# But the arguments are private, suited for this system only
def checkFolderStructure(  _mainFolderPath: str     = getGlobalVariables.mainFolderPath,
                           _inputFolderPath: str    = getGlobalVariables.inputFolderPath,
                           _outputFolderPath: str   = getGlobalVariables.outputFolderPath) -> bool: 
    print("Hello from {0}".format(__name__))
    print("_mainFolderPath:", _mainFolderPath)
    print("_outputFolderPath:", _outputFolderPath)

    # Making overall folders if absent
    inputFolderPathSetupStatus  = ifNotFolderThenCreate(_FolderPath = _inputFolderPath)
    outputFolderPathSetupStatus = ifNotFolderThenCreate(_FolderPath = _outputFolderPath)

    presentStatus = inputFolderPathSetupStatus and outputFolderPathSetupStatus
    mappingFolderStructureStatus = False
    if presentStatus:
        mappingFolderStructureStatus = mappingFolderStructure(_mapStartFolderPath = _inputFolderPath, _mapEndFolderPath = _outputFolderPath)
    # End of 'if presentStatus:'

    presentStatus = presentStatus and mappingFolderStructureStatus
    
    return presentStatus
# End of 'def checkFolderStructure():'