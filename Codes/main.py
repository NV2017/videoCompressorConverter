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
        self._logErrorProgram   = logErrorProgram

        self.screenWidth    = self.tkFrameRoot.winfo_screenwidth()
        self.screenHeight   = self.tkFrameRoot.winfo_screenheight()
        self.screenFraction = getGlobalVariables.GUIscreenFraction

        self._setTkAppWindowSize    = pureTkGUIfunctions._setTkAppWindowSize
    # End of 'def __init__(self, parent):'

    def startApp(self):
        # Set Tkinter App Title
        setTkFrameNameStatus = self.setTkFrameName( _run        = True,
                                                    name        = self.AppName,
                                                    tkFrameRoot = self.tkFrameRoot)
        print("setTkFrameNameStatus:", setTkFrameNameStatus)

        # Set Tkinter App Window Size on device
        setTkAppWindowSizeStatus = self.setTkAppWindowSize( _run            = setTkFrameNameStatus,
                                                            GUIscreenWidth  = self.screenWidth,
                                                            GUIscreenHeight = self.screenHeight,
                                                            screenFraction  = self.screenFraction)
        print("setTkAppWindowSizeStatus:", setTkAppWindowSizeStatus)

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

            tempLogError = self._logErrorProgram(   _logFolderPath      = getGlobalVariables.errorFolderPath,
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
    # End of 'def setTkFrameName( self, _run:bool = None, name:str = None, tkFrameRoot = None):'

    def setTkAppWindowSize( self, _run:bool = None, GUIscreenWidth:int = None, GUIscreenHeight:int = None, screenFraction:float = None):
        try:
            tempInputVariablesStr = "[_run, GUIscreenWidth, GUIscreenHeight, screenFraction]"
            tempInputVariables = eval(tempInputVariablesStr)
            if None in tempInputVariables:
                list(map(lambda item: print("Blank: {0}: {1}, file: {2}, function: {3}".format(tempInputVariablesStr.replace("[","").replace("]","").split(",")[item[0]], item[1], __name__, MainApplication.setTkFrameName.__name__)) if item[1] == None else None, enumerate(tempInputVariables)))
                return False
            # End of 'if None in [_run, name]:'

            if not _run:
                print("No permission to run function: {0} in file: {1}, skipping".format(MainApplication.setTkAppWindowSize.__name__, __name__))
                return False
            # End of 'if not _run:'
            
            tempWidthInt    = min(int(GUIscreenWidth    *screenFraction), GUIscreenWidth)
            tempHeightInt   = min(int(GUIscreenHeight   *screenFraction), GUIscreenHeight)

            self._setTkAppWindowSize(tkFrameRoot = self.tkFrameRoot, width = tempWidthInt, height = tempHeightInt)
            
            return True
        except Exception as setTkAppWindowSizeError:
            tempErrorText = "setTkAppWindowSizeError: {0}".format(setTkAppWindowSizeError)

            print(tempErrorText)

            tempLogError = self._logErrorProgram(   _logFolderPath      = getGlobalVariables.errorFolderPath,
                                                    _logFilepath        = getGlobalVariables.errorFilePath,
                                                    _logMessage         = tempErrorText,
                                                    _logFilename        = getGlobalVariables.errorFileName,
                                                    _logFolderStatus    = True,
                                                    _logActionCode      = getGlobalVariables.setTkAppWindowSizeErrorUID,
                                                    _fromFile           = __name__,
                                                    _crticalErrorPath   = getGlobalVariables.mainCodesFolderPath,
                                                    _type               = getGlobalVariables.errorStr
                                                )

            return False
        # End of 'try:'
    # End of 'def setTkFrameName( self, _run:bool = None, name:str = None, tkFrameRoot = None):'

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
