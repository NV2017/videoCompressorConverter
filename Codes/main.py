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
        self._logErrorProgram   = logErrorProgram

        self.tkFrameRoot    = tk.Tk()

        self.AppName            = AppName        
        self._setTkFrameName    = pureTkGUIfunctions._setTkFrameName

        self.screenWidth    = self.tkFrameRoot.winfo_screenwidth()
        self.screenHeight   = self.tkFrameRoot.winfo_screenheight()
        self.screenFraction = getGlobalVariables.GUIscreenFraction

        self._setTkAppWindowSize    = pureTkGUIfunctions._setTkAppWindowSize

        self.MenuBar            = Menu(self.tkFrameRoot)
        self.GUImenuButtons     = getGlobalVariables.GUImenuButtons
        self._addTkAppMenuBar   = pureTkGUIfunctions._addTkAppMenuBar
    # End of 'def __init__(self, parent):'

    def startApp(self):
        # Under the hood, the following are components that make the App
        # This function is not wrapped in try/catch/exception because
        # Because each of the statements themselves are wrapped in try/catch/exception
        # The steps are permissioned, i.e. require '_run' to be True
        # Each step in the sequence below returns Tru/False, depending on it's completion status
        # Therefore, steps are sequentially run if & only if the previous step an sans error
        # All errors with unique UIDs are recorded inside the error folder in csv rows, daily new file
        # Likewise, important logs are also recorded inside the log folder in csv rows, daily new file

        # Theme is added to a simple Menu bar cascade option

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

        # Add a DemoObject
        addTkAppDemoObjectStatus, DemoObject = self.addTkAppDemoObject(_run = setTkAppWindowSizeStatus, InternalThemeState = True)
        print("addTkAppDemoObjectStatus:", addTkAppDemoObjectStatus)

        # Add Menubar
        addTkAppMenuBarStatus, addTkAppMenuBarInternalThemeState = self.addTkAppMenuBar(_run = addTkAppDemoObjectStatus, MenuBar = self.MenuBar, Buttons = self.GUImenuButtons, DemoObject = DemoObject)
        print("addTkAppMenuBarStatus:", addTkAppMenuBarStatus)

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
                list(map(lambda item: print("Blank: {0}: {1}, file: {2}, function: {3}".format(tempInputVariablesStr.replace("[","").replace("]","").split(",")[item[0]], item[1], __name__, MainApplication.setTkAppWindowSize.__name__)) if item[1] == None else None, enumerate(tempInputVariables)))
                return False
            # End of 'if None in [_run, name]:'

            if not _run:
                print("No permission to run function: {0} in file: {1}, skipping".format(MainApplication.setTkAppWindowSize.__name__, __name__))
                return False
            # End of 'if not _run:'
            
            tempWidthInt    = int(GUIscreenWidth    *screenFraction)
            tempHeightInt   = int(GUIscreenHeight   *screenFraction)

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

    def addTkAppDemoObject( self, _run:bool = None, InternalThemeState:bool = None):
        try:
            tempInputVariablesStr = "[_run, InternalThemeState]"
            tempInputVariables = eval(tempInputVariablesStr)
            if None in tempInputVariables:
                list(map(lambda item: print("Blank: {0}: {1}, file: {2}, function: {3}".format(tempInputVariablesStr.replace("[","").replace("]","").split(",")[item[0]], item[1], __name__, MainApplication.addTkAppDemoObject.__name__)) if item[1] == None else None, enumerate(tempInputVariables)))
                return False
            # End of 'if None in [_run, name]:'

            if not _run:
                print("No permission to run function: {0} in file: {1}, skipping".format(MainApplication.addTkAppDemoObject.__name__, __name__))
                return False
            # End of 'if not _run:'

            # self._addTkAppDemoObject(tkFrameRoot = self.tkFrameRoot)
            # print("addTkAppDemoObject InternalThemeState:", InternalThemeState)
            DemoObject = Label(text="Demo Button")
            tempColor = "yellow" if InternalThemeState else "green"
            print("addTkAppDemoObject InternalThemeState: {0}, tempColor:{1}".format(InternalThemeState, tempColor))
            DemoObject.config(fg=tempColor)
            DemoObject.pack()
            
            return True, DemoObject
        except Exception as addTkAppDemoObjectError:
            tempErrorText = "addTkAppDemoObjectError: {0}".format(addTkAppDemoObjectError)

            print(tempErrorText)

            tempLogError = self._logErrorProgram(   _logFolderPath      = getGlobalVariables.errorFolderPath,
                                                    _logFilepath        = getGlobalVariables.errorFilePath,
                                                    _logMessage         = tempErrorText,
                                                    _logFilename        = getGlobalVariables.errorFileName,
                                                    _logFolderStatus    = True,
                                                    _logActionCode      = getGlobalVariables.addTkAppDemoObjectErrorUID,
                                                    _fromFile           = __name__,
                                                    _crticalErrorPath   = getGlobalVariables.mainCodesFolderPath,
                                                    _type               = getGlobalVariables.errorStr
                                                )

            return False
        # End of 'try:'
    # End of 'def addTkAppMenuBar( self, _run:bool = None):'

    def addTkAppMenuBar( self, _run:bool = None, MenuBar = None, Buttons:list = None, DemoObject = None):
        try:
            tempInputVariablesStr = "[_run, MenuBar, Buttons, DemoObject]"
            tempInputVariables = eval(tempInputVariablesStr)
            if None in tempInputVariables:
                list(map(lambda item: print("Blank: {0}: {1}, file: {2}, function: {3}".format(tempInputVariablesStr.replace("[","").replace("]","").split(",")[item[0]], item[1], __name__, MainApplication.addTkAppMenuBar.__name__)) if item[1] == None else None, enumerate(tempInputVariables)))
                return False
            # End of 'if None in [_run, name]:'

            if not _run:
                print("No permission to run function: {0} in file: {1}, skipping".format(MainApplication.addTkAppMenuBar.__name__, __name__))
                return False
            # End of 'if not _run:'

            addTkAppMenuBarInternalThemeState = self._addTkAppMenuBar(tkFrameRoot = self.tkFrameRoot, MenuBar = MenuBar, Buttons = Buttons, DemoObject = DemoObject)
            # print("addTkAppMenuBar addTkAppMenuBarInternalThemeState:", addTkAppMenuBarInternalThemeState)
            
            return True, addTkAppMenuBarInternalThemeState
        except Exception as addTkAppMenuBarError:
            tempErrorText = "addTkAppMenuBarError: {0}".format(addTkAppMenuBarError)

            print(tempErrorText)

            tempLogError = self._logErrorProgram(   _logFolderPath      = getGlobalVariables.errorFolderPath,
                                                    _logFilepath        = getGlobalVariables.errorFilePath,
                                                    _logMessage         = tempErrorText,
                                                    _logFilename        = getGlobalVariables.errorFileName,
                                                    _logFolderStatus    = True,
                                                    _logActionCode      = getGlobalVariables.addTkAppMenuBarUID,
                                                    _fromFile           = __name__,
                                                    _crticalErrorPath   = getGlobalVariables.mainCodesFolderPath,
                                                    _type               = getGlobalVariables.errorStr
                                                )

            return False
        # End of 'try:'
    # End of 'def addTkAppMenuBar( self, _run:bool = None):'    

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
