# checkFolderStructure.py

from imports import *

# Given a path, this function creates folder if absent
def ifNotFolderThenCreate(_FolderPath: str) -> bool: # Sort of private function, not used elsewhere
    try:
        if not os.path.exists(_FolderPath):
            os.mkdir(_FolderPath)
            print("Created folder path: {0}".format(_FolderPath))
        else:
            print("Detected folder path: {0}".format(_FolderPath))
        # End of 'if not os.path.exists(_FolderPath):'
        return True
    except:
        print("Error detecting folder path: {0}".format(_FolderPath))
        return False
    # End of 'try:'
# End of 'def ifNotFolderThenCreate(_FolderPath):'

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
    
    return presentStatus
# End of 'def checkFolderStructure():'