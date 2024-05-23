# fileLoopFFMPEGconverterCompressor.py

from imports import *

def absoluteFilePaths(_directory:str = None):
    absoluteFilePathsList = []
    for dirpath, _, filenames in os.walk(_directory):
        absoluteFilePathsList += list(map(lambda x: os.path.abspath(os.path.join(dirpath, x)), filenames))
    # End of 'for dirpath, _, filenames in os.walk(_directory):'
    return absoluteFilePathsList
# End of 'def absoluteFilePaths(_directory:str):'

def ifFilesExistInTheInputFolder(_inputFolderPath:str = None):
    if _inputFolderPath == None:
        print("Blank input in {0}, skipping".format(ifFilesExistInTheInputFolder.__name__))
        return False, []
    # End of 'if _inputFolderPath == None:'

    try:
        absoluteFilepaths       = [item for item in absoluteFilePaths(_directory = _inputFolderPath)]
        absoluteFilepathsCount  = len(absoluteFilepaths)
        if absoluteFilepathsCount == 0:
            print("No files detected in input folder at: {0}, from file: {1}, quitting".format(_inputFolderPath, __name__))
            return True, []
        else:
            print("{0} files detected in input folder at: {0}, from file: {1}".format(absoluteFilepathsCount, _inputFolderPath, __name__))
        # End of 'if absoluteFilepathsCount == 0:'
        return True, absoluteFilepaths
    except Exception as ifFilesExistInInputFolderError:
        tempErrorText = ("{0}_Error in detecting any files from: {1}, file: {2}. Error: {3}".format(getGlobalVariables.ifFilesExistInInputFolderErrorUID, 
                                                                                                    _inputFolderPath,
                                                                                                    __name__, 
                                                                                                    ifFilesExistInInputFolderError))
        print(tempErrorText)

        tempLogError = logErrorProgram (_logFolderPath      = getGlobalVariables.errorFolderPath,
                                        _logFilepath        = getGlobalVariables.errorFilePath,
                                        _logMessage         = tempErrorText,
                                        _logFilename        = getGlobalVariables.errorFileName,
                                        _logFolderStatus    = True,
                                        _logActionCode      = getGlobalVariables.ifFilesExistInInputFolderErrorUID,
                                        _fromFile           = __name__,
                                        _crticalErrorPath   = getGlobalVariables.mainCodesFolderPath,
                                        _type               = getGlobalVariables.errorStr
                                        )

        return False, []
    # End of 'try:
# End of 'def ifFilesExistInTheInputFolder(_inputFolderPath:str = None):'

def fileLoopFFMPEGconverterCompressor(inputFolderPath: str = None, outputFolderPath: str = None):
    if None in [inputFolderPath, outputFolderPath]:
        if inputFolderPath  == None: print("Blank: {0}, file: {1}".format(inputFolderPath,  __name__))
        if outputFolderPath == None: print("Blank: {0}, file: {1}".format(outputFolderPath, __name__))
        return True
    # End of 'if None in [inputFolderPath, outputFolderPath]:'

    # Find if files exist in the input folder
    ifFilesExistInTheInputFolderStatus, absoluteFilepaths = ifFilesExistInTheInputFolder(_inputFolderPath = getGlobalVariables.inputFolderPath)
    print("ifFilesExistInTheInputFolderStatus:", ifFilesExistInTheInputFolderStatus)

    
    # print("absoluteFilepaths:",absoluteFilepaths)
    print("To Code")
    
# End of 'def fileLoopFFMPEGconverterCompressor():'