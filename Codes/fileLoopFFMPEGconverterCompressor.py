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

def absoluteFilepathsEndWithAppropriateExtension(absoluteFilepaths:list = None, extensionsAllowed = None):
    extensionsOfFilesBoolean = list(map(lambda x:"."+x.split(".")[-1].lower() in extensionsAllowed, absoluteFilepaths))
    return list(compress(absoluteFilepaths, extensionsOfFilesBoolean))
# End of 'def absoluteFilepathsEndWithAppropriateExtension(absoluteFilepaths:list = []):'

def permissionedAbsoluteFilepathsEndWithAppropriateExtension(_run:bool = None, _absoluteFilepaths:list = None):
    if None in [_run, _absoluteFilepaths]:
        if _run                 == None: print("Blank: _run: {0}, file: {1}"                .format(_run,  __name__))
        if _absoluteFilepaths   == None: print("Blank: _absoluteFilepaths: {0}, file: {1}"  .format(_absoluteFilepaths,    __name__))
        return False, []
    # End of 'if None in [_mapStartFolderPath, _mapEndFolderPath]:'

    if not _run:
        print("No permission to run {0} in {1}, skipping".format(permissionedAbsoluteFilepathsEndWithAppropriateExtension.__name__, __name__))
        return False, []
    # End of 'if not _run:'

    if _absoluteFilepaths == []:
        print("Blank _absoluteFilepaths received, can't run {0} in {1}, skipping".format(permissionedAbsoluteFilepathsEndWithAppropriateExtension.__name__, __name__))
        return False, []
    # End of 'if _absoluteFilepaths == []:'

    try:
        absoluteFilepathsEndWithAppropriateExtensionList = absoluteFilepathsEndWithAppropriateExtension(absoluteFilepaths = _absoluteFilepaths, extensionsAllowed = getGlobalVariables.acceptedInputVideoFormat)
        toReturnTrue = len(absoluteFilepathsEndWithAppropriateExtensionList) != 0
        return toReturnTrue, absoluteFilepathsEndWithAppropriateExtensionList
    except Exception as permissionedAbsoluteFilepathsEndWithAppropriateExtensionError:
        tempErrorText = ("{0}_Error in detecting any appropriate files from: {1}, file: {2}. Error: {3}".format(getGlobalVariables.permissionedAbsoluteFilepathsEndWithAppropriateExtensionErrorUID, 
                                                                                                                getGlobalVariables.inputFolderPath,
                                                                                                                __name__, 
                                                                                                                permissionedAbsoluteFilepathsEndWithAppropriateExtensionError))
        print(tempErrorText)

        tempLogError = logErrorProgram (_logFolderPath      = getGlobalVariables.errorFolderPath,
                                        _logFilepath        = getGlobalVariables.errorFilePath,
                                        _logMessage         = tempErrorText,
                                        _logFilename        = getGlobalVariables.errorFileName,
                                        _logFolderStatus    = True,
                                        _logActionCode      = getGlobalVariables.permissionedAbsoluteFilepathsEndWithAppropriateExtensionErrorUID,
                                        _fromFile           = __name__,
                                        _crticalErrorPath   = getGlobalVariables.mainCodesFolderPath,
                                        _type               = getGlobalVariables.errorStr
                                        )

        return False, []
    # End of 'try:

# End of 'def permissionedAbsoluteFilepathsEndWithAppropriateExtension(_run:bool = False, _absoluteFilepaths:list = []):'

def _permissionedDeleteEmptyFoldersInInputDirectory(_run:bool = None, _inputFolderPath:str = None):
    if None in [_run, _inputFolderPath]:
        if _run                 == None: print("Blank: _run: {0}, file: {1}"                .format(_run,               __name__))
        if _inputFolderPath     == None: print("Blank: _inputFolderPath: {0}, file: {1}"    .format(_inputFolderPath,   __name__))
        return False
    # End of 'if None in [_mapStartFolderPath, _mapEndFolderPath]:'

    # Walk through all subfolders in '_inputFolderPath', delete if they are empty
    try:
        _tempFolders = list(os.walk(_inputFolderPath, topdown=True))[1:]
        _tempFoldersLen = len(_tempFolders)
        if _tempFoldersLen == 0:
            print("No empty folders to delete in: {}".format(_inputFolderPath))
            return True
        # End of 'if _tempFoldersLen == 0:'
        _tempFolders.reverse()
        for index, item in enumerate(_tempFolders):
            if len(os.listdir(item[0])) == 0:
                os.rmdir(item[0])
                print("{0} out of {1}, deleted EMPTY folder: {2}, in: {3}, in: {4}, in: {5}".format(str(index+1), _tempFoldersLen, item[0], _inputFolderPath, _permissionedDeleteEmptyFoldersInInputDirectory.__name__, __name__))
            else:
                print("{0} out of {1}, NOT-deleted not-empty folder: {2}, in: {3}, in {4}, in: {5}".format(str(index+1), _tempFoldersLen, item[0], _inputFolderPath, _permissionedDeleteEmptyFoldersInInputDirectory.__name__, __name__))
            # End of 'if len(os.listdir(item[0])) == 0:'
        # End of 'for item in _tempFolders:'

        return True
    except Exception as permissionedDeleteEmptyFoldersInInputDirectoryError:
        tempErrorText = ("{0}_Error in deleting empty subfolders in: {1}, in: {2}, file: {3}. Error: {4}".format(   getGlobalVariables.permissionedDeleteEmptyFoldersInInputDirectoryErrorUID, 
                                                                                                                    _inputFolderPath,
                                                                                                                    _permissionedDeleteEmptyFoldersInInputDirectory.__name__,
                                                                                                                    __name__, 
                                                                                                                    permissionedDeleteEmptyFoldersInInputDirectoryError))
        print(tempErrorText)

        tempLogError = logErrorProgram (_logFolderPath      = getGlobalVariables.errorFolderPath,
                                        _logFilepath        = getGlobalVariables.errorFilePath,
                                        _logMessage         = tempErrorText,
                                        _logFilename        = getGlobalVariables.errorFileName,
                                        _logFolderStatus    = True,
                                        _logActionCode      = getGlobalVariables.permissionedDeleteEmptyFoldersInInputDirectoryErrorUID,
                                        _fromFile           = __name__,
                                        _crticalErrorPath   = getGlobalVariables.mainCodesFolderPath,
                                        _type               = getGlobalVariables.errorStr
                                        )
        return False
    # End of 'try:'
    return True
# End of 'def _permissionedDeleteEmptyFoldersInInputDirectory(_run:bool = None, _inputFolderPath:str = None):'

def fileLoopFFMPEGconverterCompressor(inputFolderPath: str = None, outputFolderPath: str = None):
    if None in [inputFolderPath, outputFolderPath]:
        if inputFolderPath  == None: print("Blank: {0}, file: {1}".format(inputFolderPath,  __name__))
        if outputFolderPath == None: print("Blank: {0}, file: {1}".format(outputFolderPath, __name__))
        return True
    # End of 'if None in [inputFolderPath, outputFolderPath]:'

    # Find if files exist in the input folder
    ifFilesExistInTheInputFolderStatus, absoluteFilepaths = ifFilesExistInTheInputFolder(_inputFolderPath = getGlobalVariables.inputFolderPath)
    
    # Filter for absolute filepaths that end with appropriate extension
    permissionedAbsoluteFilepathsEndWithAppropriateExtensionStatus, absoluteFilepathsEndWithAppropriateExtension = permissionedAbsoluteFilepathsEndWithAppropriateExtension(_run = ifFilesExistInTheInputFolderStatus, _absoluteFilepaths = absoluteFilepaths)

    # Start ffmpeg for each file, while checking formats and subtitles
    permissionedFFmpegForEachFileStatus = permissionedFFmpegForEachFile(_run = permissionedAbsoluteFilepathsEndWithAppropriateExtensionStatus, _absoluteFilepathsEndWithAppropriateExtension = absoluteFilepathsEndWithAppropriateExtension)

    # Delete every empty subdirectory inside 'inputFolderPath'
    permissionedDeleteEmptyFoldersInInputDirectoryStatus = _permissionedDeleteEmptyFoldersInInputDirectory(_run = permissionedFFmpegForEachFileStatus, _inputFolderPath = inputFolderPath)

    return permissionedDeleteEmptyFoldersInInputDirectoryStatus
# End of 'def fileLoopFFMPEGconverterCompressor():'