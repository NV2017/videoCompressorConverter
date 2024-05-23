# videoConvertorCompressor.py

from imports import *

def videoConvertorCompressor():
    try:
        # Check Input Output folder structure
        checkFolderStructureStatus = checkFolderStructure()
        print("checkFolderStructureStatus:", checkFolderStructureStatus)

        fileLoopFFMPEGconverterCompressorStatus = fileLoopFFMPEGconverterCompressor(inputFolderPath = getGlobalVariables.inputFolderPath, outputFolderPath = getGlobalVariables.outputFolderPath)
        print("fileLoopFFMPEGconverterCompressorStatus:", fileLoopFFMPEGconverterCompressorStatus)
    except Exception as videoConvertorCompressorError:
        tempErrorText = ("{0}_Unable to finish {1}, error: {2}".format(getGlobalVariables.videoConvertorCompressorErrorUID, __name__, videoConvertorCompressorError))
        print(tempErrorText)

        tempLogError = logErrorProgram (_logFolderPath      = getGlobalVariables.errorFolderPath,
                                        _logFilepath        = getGlobalVariables.errorFilePath,
                                        _logMessage         = tempErrorText,
                                        _logFilename        = getGlobalVariables.errorFileName,
                                        _logFolderStatus    = True,
                                        _logActionCode      = getGlobalVariables.videoConvertorCompressorErrorUID,
                                        _fromFile           = __name__,
                                        _crticalErrorPath   = getGlobalVariables.mainCodesFolderPath,
                                        _type               = getGlobalVariables.errorStr
                                        )
    # End of 'try:'
# End of 'def videoConvertorCompressor():'