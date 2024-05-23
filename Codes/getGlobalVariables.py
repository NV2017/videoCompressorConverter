# getGlobalVariables.py

from imports import *
from logError import _typeErrorStr, _typeLogStr

osSeparator = os.path.sep

codesFolderName     = 'Codes'
inputFolderName     = 'Input'
outputFolderName    = 'Output'
logFolderName       = 'Log'
ErrorFolderName     = 'Error'

mainCodesFolderPath = os.path.join(os.getcwd(),codesFolderName)

mainFolderPath = osSeparator.join(mainCodesFolderPath.split(osSeparator)[0:-1])

inputFolderPath = os.path.join(mainFolderPath, inputFolderName)
outputFolderPath = os.path.join(mainFolderPath, outputFolderName)
logFolderPath = os.path.join(mainFolderPath, logFolderName)
errorFolderPath = os.path.join(mainFolderPath, ErrorFolderName)

csvDotExtension = ".csv"
errorStr    = _typeErrorStr
logStr      = _typeLogStr
LogErrorS = [errorStr, logStr]

logFileName = dt.datetime.now().strftime("%Y%m%d") + "_Logs" + csvDotExtension
logFilePath = os.path.join(logFolderPath, logFileName)

errorFileName = dt.datetime.now().strftime("%Y%m%d") + "_Errors" + csvDotExtension
errorFilePath = os.path.join(errorFolderPath, errorFileName)

acceptedInputVideoFormat = ['.mp4','.avi','.mkv','.flv', '.webm', '.mov']

videoConvertorCompressorErrorUID                                    = "#000001"
checkFolderStructureErrorUID                                        = "#000002"
mappingFolderStructureErrorUID                                      = "#000003"
ifNotFolderThenCreateErrorUID                                       = "#000004"
ifFilesExistInInputFolderErrorUID                                   = "#000005"
permissionedAbsoluteFilepathsEndWithAppropriateExtensionErrorUID    = "#000006"
permissionedFFmpegForEachFileErrorUID                               = "#000007"