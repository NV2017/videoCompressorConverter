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

logFileName = dt.datetime.now().strftime("%Y%m%d") + "_" + logFolderName + csvDotExtension
logFilePath = os.path.join(logFolderPath, logFileName)

errorFileName = dt.datetime.now().strftime("%Y%m%d") + "_" + ErrorFolderName + csvDotExtension
errorFilePath = os.path.join(errorFolderPath, errorFileName)

outputVideoFormat           = ".mp4"
acceptedInputVideoFormat    = [outputVideoFormat,'.avi','.mkv','.flv', '.webm', '.mov']
subtitleExtention           = ".srt"
latestCodec                 = "libx265"
EngSubtitleStr              = "Eng Hard Subbed"

datetimePrintFormat = "%Y-%m-%d %H:%M:%S"

videoConvertorCompressorErrorUID                                    = "#000001"
checkFolderStructureErrorUID                                        = "#000002"
mappingFolderStructureErrorUID                                      = "#000003"
ifNotFolderThenCreateErrorUID                                       = "#000004"
ifFilesExistInInputFolderErrorUID                                   = "#000005"
permissionedAbsoluteFilepathsEndWithAppropriateExtensionErrorUID    = "#000006"
permissionedFFmpegForEachFileErrorUID                               = "#000007"
generateSubtitleFilePathErrorUID                                    = "#000008"
generateExpectedOutputPathErrorUID                                  = "#000009"
permissionedDeleteEmptyFoldersInInputDirectoryErrorUID              = "#000010"
ConvertNoSubtitleErrorUID                                           = "#000011"
ConvertWithSubtitleErrorUID                                         = "#000012"
GUIstartAppErrorUID                                                 = "#000013"
setTkFrameNameErrorUID                                              = "#000014"

ConvertNoSubtitleLogUID             = "#000001"
ConvertWithSubtitleLogUID           = "#000002"
DeletePreExistingOutputFileLogUID   = "#000003"

GUItkinterAppName   = "vCC 0.0.1"