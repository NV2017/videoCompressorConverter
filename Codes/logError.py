###############################################################################
############################ Program Log Record ###############################

# This file self-contained, no need to import libraries or variables from outside

# This function 'ProgramLogRecord' will take input of a directory, ideally dedicated for log entries
# Inside the above folder, it will make error entries in csv files with timestamps
# No entries made in any ddatabase. This way no database error due to this progrm possible
# Every error entry can carry a unique signature, helping isolate the source of the problem
# Returns True if log is entered, otherwise False
# Additionally, it saves messages in log folder too using the '_type' flag

import os
import time
import pandas as pd
import datetime as dt
from tzlocal import get_localzone

mainFunctionName = os.path.basename(__file__)

currentDateTime = dt.datetime.now(tz=get_localzone())
currentTimeZone = currentDateTime.strftime('%Z')

logFileColumns = ['YearMonthDay', 'HourMinuteSecond', 'TimeZone', 'TimeStampUNIX', 'LogActionCode','FromFile', 'Log']
_typeS = ['error','log']

def _MissingLogFolderAction(_tempError = "LogEntryFunctionError"):
    tempDatetimeNow = dt.datetime.now().strftime("%Y%m%d%H%M%S")
            
    tempMissingLogFolderErrorRoot = tempDatetimeNow + "_MissingLogFolder"
    tempMissingLogFolderErrorFilename = tempMissingLogFolderErrorRoot + ".txt"
    tempMissingLogFolderError = ("#000000_" + tempMissingLogFolderErrorRoot + "_" + os.path.dirname(os.path.realpath(__file__)) + "_Error: " + str(_tempError))

    tempFile = open(tempMissingLogFolderErrorFilename, "w")
    tempFile.write(tempMissingLogFolderError) 
    tempFile.close()

    print(tempMissingLogFolderError)
# End of 'def _MissingLogFolderAction():'
    
def _saveLogEntry(_logFilepath = None, _logFilename = None, _currentTimeZone = currentTimeZone, _logActionCode = None, 
                  _fromFile = None, _TimeStampUNIX = None, _logMessage = None, _logFileColumns = logFileColumns):
    
    inputCheckNotNoneList = [_logFilepath, _logFilename, _currentTimeZone, _logActionCode, _fromFile, _TimeStampUNIX, _logMessage, _logFileColumns]
    
    if not any(inputCheckNotNoneList):
        print("Wrong arguments entered in {0} function for entry"       .format(mainFunctionName))
        if (_logFilepath        is None): print("_logFilepath: {0}"     .format(_logFilepath))
        if (_logFilename        is None): print("_logFilename: {0}"     .format(_logFilename))
        if (_currentTimeZone    is None): print("_currentTimeZone: {0}" .format(_currentTimeZone))
        if (_logActionCode      is None): print("_logActionCode: {0}"   .format(_logActionCode))
        if (_fromFile           is None): print("_fromFile: {0}"        .format(_fromFile))
        if (_TimeStampUNIX      is None): print("_TimeStampUNIX: {0}"   .format(_TimeStampUNIX))
        if (_logMessage         is None): print("_logMessage: {0}"      .format(_logMessage))
        if (_logFileColumns     is None): print("_logFileColumns: {0}"  .format(_logFileColumns))
        return None
    # End of 'if not any(inputCheckNotNoneList):'
    
    # Making the row to upload on the error file
    tempNewDf = pd.DataFrame({"a": dt.datetime.now().strftime("%Y-%m-%d"),
                              "b": dt.datetime.now().strftime("%H:%M:%S"),
                              "c": _currentTimeZone,
                              "d": _TimeStampUNIX,
                              "e": _logActionCode,
                              "f": _fromFile,
                              "g": _logMessage},
                              index=[0])
    tempNewDf.columns = _logFileColumns
    
    if(os.path.isfile(_logFilepath)):
        tempOldDf = pd.read_csv(_logFilepath)
    else:
        tempOldDf = pd.DataFrame({"a": dt.datetime.now().strftime("%Y-%m-%d"),
                                  "b": dt.datetime.now().strftime("%H:%M:%S"),
                                  "c": _currentTimeZone,
                                  "d": _TimeStampUNIX,
                                  "e": _logActionCode,
                                  "f": _fromFile,
                                  "g": _logMessage},
                                  index=[])
        tempOldDf.columns = _logFileColumns
    # End of 'if(os.path.isfile(__logFilepath)):'
    
    if len(tempOldDf) == 0:
        _tempDfOutput = tempNewDf
    else:
        _tempDfOutput = pd.concat([tempOldDf, tempNewDf], ignore_index=True)
    # End of 'if len(tempOldDf) == 0:'
    
    if(os.path.isfile(_logFilepath)):
        os.remove(_logFilepath)
    # End of 'if(os.path.isfile(__logFilepath)):'
    
    _tempDfOutput.to_csv(_logFilepath, index = False)
    return None
# End of 'def _saveLogEntry()'

def logErrorProgram(_logFolderPath:    str = None,                      # Name of the folder where log is going to be saved
                    _logFilepath:      str = None,                      # Path of the file where log is going to be saved
                    _logMessage:       str = "No Error Message",        # The actual log message
                    _logFilename:      str = None,                      # Name of the file where log is going to be saved
                    _logFolderStatus: bool = False,                     # If False, then this function doesn't run
                    _logActionCode:    str = None,                      # A code that is logged, ideally different when called from different code blocks
                    _fromFile:         str = None,                      # Name of the File from which this log for error is called
                    _crticalErrorPath: str = None,                      # When can't find csv for logging error, save a .txt in this path
                    _logFileColumns:  list = logFileColumns,            # The columns in the output file, imported from above
                    _currentTimeZone:  str = currentTimeZone,
                    _type:             str = None) -> bool:  # Time zone of where this script is running, from the OS/Server/PC
    try:
        inputCheckNotNoneList = [_logFolderPath, _logFilepath, _logFilename, _logFolderStatus, _logActionCode, _fromFile, _crticalErrorPath, _type]
        
        if not any(inputCheckNotNoneList):
            print("No arguments entered in log records function for entry")
            return False
        # End of 'if():'
        
        if (not _logFolderStatus):
            print("Log entry {0} skipped, for folder: {1}, due to status: {2}".format(_logMessage, _logFolderPath, _logFolderStatus))
            return False
        # End of 'if(not _logFolderStatus):'

        # Checking _type as 'error' or 'log'
        if _type not in _typeS:
            print("Log entry {0} skipped, for folder: {1}, due to _type: {2} not in {3}".format(_logMessage, _logFolderPath, _type, _logFolderStatus))
            return False
        # End of 'if _type not in _typeS:'

        _currentTimeStampUNIX = int(time.mktime(dt.datetime.now().timetuple()))
        
        _saveLogEntry(_logFilepath      = _logFilepath,
                      _logFilename      = _logFilename,
                      _currentTimeZone  = _currentTimeZone,
                      _logActionCode    = _logActionCode,
                      _fromFile         = _fromFile,
                      _TimeStampUNIX    = _currentTimeStampUNIX,
                      _logMessage       = _logMessage,
                      _logFileColumns   = _logFileColumns)
        
        return True
    except Exception as LogEntryFunctionError:
        _MissingLogFolderAction(_tempError = LogEntryFunctionError)
        return False
    # End of 'try:'
# End of 'def logErrorProgram():'

####################### End of 'Program Log Record' ###########################
###############################################################################