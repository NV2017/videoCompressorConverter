# FFmpy_Codes.py

from imports import *

def generateSubtitleFilePath(_inputFilePath:str = None, _subtitleExtention:str = None):
    if None in [_inputFilePath, _subtitleExtention]:
        if _inputFilePath       == None: print("Blank: {0}, file: {1}".format(_inputFilePath,  __name__))
        if _subtitleExtention   == None: print("Blank: {0}, file: {1}".format(_subtitleExtention, __name__))
        return False, None
    # End of 'if None in [inputFolderPath, outputFolderPath]:'
    
    try:
        # Generate the extention file
        subtitleFilepath = _inputFilePath.rsplit(".",1)[0] + _subtitleExtention
        return True, subtitleFilepath
    except Exception as generateSubtitleFilePathError:
        tempErrorText = ("{0}_Error from: {1}, file: {2}. Error: {3}".format(   getGlobalVariables.generateSubtitleFilePathErrorUID, 
                                                                                _inputFilePath,
                                                                                __name__, 
                                                                                generateSubtitleFilePathError))
        print(tempErrorText)

        tempLogError = logErrorProgram (_logFolderPath      = getGlobalVariables.errorFolderPath,
                                        _logFilepath        = getGlobalVariables.errorFilePath,
                                        _logMessage         = tempErrorText,
                                        _logFilename        = getGlobalVariables.errorFileName,
                                        _logFolderStatus    = True,
                                        _logActionCode      = getGlobalVariables.generateSubtitleFilePathErrorUID,
                                        _fromFile           = __name__,
                                        _crticalErrorPath   = getGlobalVariables.mainCodesFolderPath,
                                        _type               = getGlobalVariables.errorStr
                                        )

        return False, None
    # End of 'try:'
# End of 'def generateSubtitleFilePath(_input:str = None, _subtitleExtention:str = None):'

def generateExpectedOutputPath( _run:bool = None, _subtitleExists:bool = None, _inputFilePath:str = None, _inputFolderName:str = None, 
                                _outputFolderName:str = None, _latestCodec:str = None, _outputVideoFormat:str = None):
    if None in [_run, _subtitleExists, _inputFilePath]:
        if _run                 == None: print("Blank: {0}, file: {1}".format(_run,                 __name__))
        if _subtitleExists      == None: print("Blank: {0}, file: {1}".format(_subtitleExists,      __name__))
        if _inputFilePath       == None: print("Blank: {0}, file: {1}".format(_inputFilePath,       __name__))
        if _inputFolderName     == None: print("Blank: {0}, file: {1}".format(_inputFolderName,     __name__))
        if _outputFolderName    == None: print("Blank: {0}, file: {1}".format(_outputFolderName,    __name__))
        if _latestCodec         == None: print("Blank: {0}, file: {1}".format(_latestCodec,         __name__))
        if _outputVideoFormat   == None: print("Blank: {0}, file: {1}".format(_outputVideoFormat,   __name__))
        return False, None
    # End of 'if None in [inputFolderPath, outputFolderPath]:'

    if not _run:
        print("No permission to run {0} in {1}, skipping".format(generateExpectedOutputPath.__name__, __name__))
        return False, None
    # End of 'if not _run:'

    try:
        _tempExtension = ", codec {0}{1}".format(_latestCodec,_outputVideoFormat)
        outputFilePath =    (
                            _inputFilePath.replace(_inputFolderName, _outputFolderName).rsplit(".",1)[0] + ", {0},".format(getGlobalVariables.EngSubtitleStr) + "{0}".format(_tempExtension)
                            if _subtitleExists else
                            _inputFilePath.replace(_inputFolderName, _outputFolderName).rsplit(".",1)[0] + "{0}".format(_tempExtension)
                            )
        return False, outputFilePath
    except Exception as generateExpectedOutputPathError:
        tempErrorText = ("{0}_Error from: {1}, file: {2}. Error: {3}".format(   getGlobalVariables.generateExpectedOutputPathErrorUID, 
                                                                                generateExpectedOutputPath.__name__,
                                                                                __name__, 
                                                                                generateExpectedOutputPathError))
        print(tempErrorText)

        tempLogError = logErrorProgram (_logFolderPath      = getGlobalVariables.errorFolderPath,
                                        _logFilepath        = getGlobalVariables.errorFilePath,
                                        _logMessage         = tempErrorText,
                                        _logFilename        = getGlobalVariables.errorFileName,
                                        _logFolderStatus    = True,
                                        _logActionCode      = getGlobalVariables.generateExpectedOutputPathErrorUID,
                                        _fromFile           = __name__,
                                        _crticalErrorPath   = getGlobalVariables.mainCodesFolderPath,
                                        _type               = getGlobalVariables.errorStr
                                        )

        return False, None
    # End of 'try:'
# End of 'def generateExpectedOutputPath(_run:bool = None, _subtitleExists:bool = None):

def permissionedFFmpegForEachFile(_run:bool = None, _absoluteFilepathsEndWithAppropriateExtension:list[str] = None):
    if None in [_run, _absoluteFilepathsEndWithAppropriateExtension]:
        if _run == None: print("Blank: _run: {0}, file: {1}"                                                                                    .format(_run,  __name__))
        if _absoluteFilepathsEndWithAppropriateExtension   == None: print("Blank: _absoluteFilepathsEndWithAppropriateExtension: {0}, file: {1}".format(_absoluteFilepathsEndWithAppropriateExtension, __name__))
        return True
    # End of 'if None in [_run, _absoluteFilepathsEndWithAppropriateExtension]:'

    if not _run:
        print("No permission to run {0} in {1}, skipping".format(permissionedFFmpegForEachFile.__name__, __name__))
        return False
    # End of 'if not _run:'

    _absoluteFilepathsEndWithAppropriateExtensionLen = len(_absoluteFilepathsEndWithAppropriateExtension)
    if _absoluteFilepathsEndWithAppropriateExtensionLen == 0:
        print("No input list received in {0} in file {1}, skipping".format(permissionedFFmpegForEachFile.__name__, __name__))
        return False
    # End of 'if _absoluteFilepathsEndWithAppropriateExtensionLen == 0:'

    try:
        # Loop over each file
        for i1, item in enumerate(_absoluteFilepathsEndWithAppropriateExtension):
            runningIndex = i1 + 1
            runningIndexStr = str(runningIndex)
            print("{0} out of {1}, input received, filepath: {2}, in function: {3}, file: {4}".format(  runningIndexStr, 
                                                                                                        _absoluteFilepathsEndWithAppropriateExtensionLen,
                                                                                                        item,
                                                                                                        permissionedFFmpegForEachFile.__name__,
                                                                                                        __name__))

            # Check if subtitle filepath exists
            generateSubtitleFilePathStatus, subtitleFilePath = generateSubtitleFilePath(_inputFilePath = item, _subtitleExtention = getGlobalVariables.subtitleExtention)
            
            subtitleExists = os.path.exists(subtitleFilePath) if generateSubtitleFilePathStatus else False
            
            expectedOutputPathStatus, expectedOutputPath = generateExpectedOutputPath(  _run                = generateSubtitleFilePathStatus, 
                                                                                        _subtitleExists     = subtitleExists, 
                                                                                        _inputFilePath      = item,
                                                                                        _inputFolderName    = getGlobalVariables.inputFolderName,
                                                                                        _outputFolderName   = getGlobalVariables.outputFolderName,
                                                                                        _latestCodec        = getGlobalVariables.latestCodec,
                                                                                        _outputVideoFormat  = getGlobalVariables.outputVideoFormat)

            print("{0} out of {1}, subtitle file found: {2}".format(runningIndexStr, _absoluteFilepathsEndWithAppropriateExtensionLen, subtitleFilePath)) if subtitleExists else print("{0} out of {1}, subtitle file NOT found for: {2}".format(runningIndexStr, _absoluteFilepathsEndWithAppropriateExtensionLen, item))
            
            if subtitleExists:
                # ffmpegConvertFileWhenSubtitleExistsStatus = ffmpegConvertFileWhenSubtitleExists()
                print("Yet to Code subtitleExists")
            else:
                try:
                    # Convert
                    ff = FFmpeg(inputs={item: None},
                                outputs={expectedOutputPath: '-c:v {0}'.format(getGlobalVariables.latestCodec)}
                                )
                    tempStartTime = dt.datetime.now()
                    ff.run()

                    # Deleting input file, if it exists
                    if os.path.exists(item):
                        os.remove(item)
                    # End of 'if os.path.exists(item):'
                    tempEndTime = dt.datetime.now()

                    tempLogText = ("{0}_Log, converted {1}, to: {2}, in: {3}, in: {4}, at: {5}, in: {6} seconds".format(getGlobalVariables.ConvertNoSubtitleLogUID,
                                                                                                                        item,
                                                                                                                        expectedOutputPath,
                                                                                                                        permissionedFFmpegForEachFile.__name__,
                                                                                                                        __name__, 
                                                                                                                        tempEndTime.strftime(getGlobalVariables.datetimePrintFormat),
                                                                                                                        (tempEndTime-tempStartTime).seconds))
                    print(tempLogText)

                    tempLogError = logErrorProgram (_logFolderPath      = getGlobalVariables.logFolderPath,
                                                    _logFilepath        = getGlobalVariables.logFilePath,
                                                    _logMessage         = tempLogText,
                                                    _logFilename        = getGlobalVariables.logFileName,
                                                    _logFolderStatus    = True,
                                                    _logActionCode      = getGlobalVariables.ConvertNoSubtitleLogUID,
                                                    _fromFile           = __name__,
                                                    _crticalErrorPath   = getGlobalVariables.mainCodesFolderPath,
                                                    _type               = getGlobalVariables.logStr
                                                    )
                except Exception as ConvertNoSubtitleError:
                    tempErrorText = ("{0}_Error in converting {1}, to: {2}, in: {3}, in: {4}. Error: {5}".format(   getGlobalVariables.ConvertNoSubtitleErrorUID,
                                                                                                                    item,
                                                                                                                    expectedOutputPath,
                                                                                                                    permissionedFFmpegForEachFile.__name__,
                                                                                                                    __name__, 
                                                                                                                    ConvertNoSubtitleError))
                    print(tempErrorText)

                    tempLogError = logErrorProgram (_logFolderPath      = getGlobalVariables.errorFolderPath,
                                                    _logFilepath        = getGlobalVariables.errorFilePath,
                                                    _logMessage         = tempErrorText,
                                                    _logFilename        = getGlobalVariables.errorFileName,
                                                    _logFolderStatus    = True,
                                                    _logActionCode      = getGlobalVariables.ConvertNoSubtitleErrorUID,
                                                    _fromFile           = __name__,
                                                    _crticalErrorPath   = getGlobalVariables.mainCodesFolderPath,
                                                    _type               = getGlobalVariables.errorStr
                                                    )
                # End of 'try:'
            # End of 'if subtitleExists:'                                                                                           
        # End of 'for i1, item in enumerate(_absoluteFilepathsEndWithAppropriateExtension):'

        return True
    except Exception as permissionedFFmpegForEachFileError:
        tempErrorText = ("{0}_Error in {1}, file: {2}. Error: {3}".format(  getGlobalVariables.permissionedFFmpegForEachFileErrorUID,
                                                                            permissionedFFmpegForEachFile.__name__,
                                                                            __name__, 
                                                                            permissionedFFmpegForEachFileError))
        print(tempErrorText)

        tempLogError = logErrorProgram (_logFolderPath      = getGlobalVariables.errorFolderPath,
                                        _logFilepath        = getGlobalVariables.errorFilePath,
                                        _logMessage         = tempErrorText,
                                        _logFilename        = getGlobalVariables.errorFileName,
                                        _logFolderStatus    = True,
                                        _logActionCode      = getGlobalVariables.permissionedFFmpegForEachFileErrorUID,
                                        _fromFile           = __name__,
                                        _crticalErrorPath   = getGlobalVariables.mainCodesFolderPath,
                                        _type               = getGlobalVariables.errorStr
                                        )

        return False
    # End of 'try:'

    return False
# End of 'def permissionedFFmpegForEachFile(_absoluteFilepathsEndWithAppropriateExtension:List[str] = None):'