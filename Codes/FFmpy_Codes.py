# FFmpy_Codes.py

from imports import *

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
            print("{0} out of {1}, input received, filepath: {2}, in function: {3}, file: {4}".format(  str(i1+1), 
                                                                                                        _absoluteFilepathsEndWithAppropriateExtensionLen,
                                                                                                        item,
                                                                                                        permissionedFFmpegForEachFile.__name__,
                                                                                                        __name__))

            print("Yet to Code")                                                                                                    
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