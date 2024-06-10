# main.py

# The Goal of this program is:
# 1. to convert and compress videos
# 2. convert to libx265 for compression
# 3. covert to .mp4, as many apps play it directly sans downloading into the device
# 4. If subtitle, hard-sub it
# 5. In future, develop a UI front-end

from imports import *

class MainApplication():
    def __init__(self, AppName):
        self.AppName            = AppName
        self.tkFrameRoot        = tk.Tk()
        self._setTkFrameName    = pureTkGUIfunctions._setTkFrameName
        self.screen_width       = self.tkFrameRoot.winfo_screenwidth()
        self.screen_height      = self.tkFrameRoot.winfo_screenheight()
    # End of 'def __init__(self, parent):'

    def startApp(self):
        # Set App Title
        setTkFrameNameStatus = self.setTkFrameName( _run        = False,
                                                    name        = self.AppName,
                                                    tkFrameRoot = self.tkFrameRoot)
        print("setTkFrameNameStatus:", setTkFrameNameStatus)

        print("Started")
        self.tkFrameRoot.mainloop()
    # End of 'def startApp(self):'

    def setTkFrameName( self, _run:bool = None, name:str = None, tkFrameRoot = None):
        try:
            tempInputVariablesStr = "[_run, name, tkFrameRoot]"
            tempInputVariables = eval(tempInputVariablesStr)
            if None in tempInputVariables:
                list(map(lambda item: print("Blank: {0}: {1}, file: {2}, function: {3}".format(tempInputVariablesStr.replace("[","").replace("]","").split(",")[item[0]], item[1], __name__, MainApplication.setTkFrameName.__name__)) if item[1] == None else None, enumerate(tempInputVariables)))
                return False
            # End of 'if None in [_run, name]:'

            if not _run:
                print("No permission to run function: {0} in file: {1}, skipping".format(MainApplication.setTkFrameName.__name__, __name__))
                return False
            # End of 'if not _run:'
            
            self._setTkFrameName(name = self.AppName, tkFrameRoot = self.tkFrameRoot)
            
            return True
        except Exception as setTkFrameNameError:
            tempErrorText = "setTkFrameNameError: {0}".format(setTkFrameNameError)

            print(tempErrorText)

            tempLogError = logErrorProgram (_logFolderPath      = getGlobalVariables.errorFolderPath,
                                            _logFilepath        = getGlobalVariables.errorFilePath,
                                            _logMessage         = tempErrorText,
                                            _logFilename        = getGlobalVariables.errorFileName,
                                            _logFolderStatus    = True,
                                            _logActionCode      = getGlobalVariables.setTkFrameNameErrorUID,
                                            _fromFile           = __name__,
                                            _crticalErrorPath   = getGlobalVariables.mainCodesFolderPath,
                                            _type               = getGlobalVariables.errorStr
                                            )

            return False
        # End of 'try:'
    # End of 'def setTkFrameName(tkFrame, name):'

    def _logErrorProgram(self):
        self._logErrorProgramStatus = logErrorProgram()
    # End of 'def _logErrorProgram(self):

# End of 'class MainApplication(tk.Frame):'

if __name__ == "__main__":
    utcTimezone = pytz.utc
    timeStart = dt.datetime.now(utcTimezone)
    print("Program {0} started at: {1}".format(__name__, 
                                        timeStart.strftime("%y-%m-%d %H:%M:%S")))

    AppObject = MainApplication(AppName = getGlobalVariables.GUItkinterAppName)
    AppObject.startApp()

    timeEnd = dt.datetime.now(utcTimezone)
    print("Program {0} ended at: {1}, in {2} seconds".format(   __name__, 
                                                                timeEnd.strftime("%y-%m-%d %H:%M:%S"),
                                                                (timeEnd-timeStart).total_seconds()))
    del([utcTimezone,timeStart,timeEnd])
# End of 'if __name__ == "__main__":'
