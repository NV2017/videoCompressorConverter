# main.py

# The Goal of this program is:
# 1. to convert and compress videos
# 2. convert to libx265 for compression
# 3. covert to .mp4, as many apps play it directly sans downloading into the device
# 4. If subtitle, hard-sub it
# 5. In future, develop a UI front-end

from imports import *

# class MainApplication(tk.Frame):
#     def __init__(self, parent, AppName):
#         tk.Frame.__init__(self, parent)
#         self.parent     = parent
#         self.AppName    = AppName
#     # End of 'def __init__(self, parent):'
# # End of 'class MainApplication(tk.Frame):'


# if __name__ == "__main__":
#     root = tk.Tk()
#     MainApplication(root, AppName="asdf").pack(side="top", fill="both", expand=True)
#     root.title('PythonGuides')
#     root.geometry('400x300')
#     root.mainloop()
# # End of 'if __name__ == "__main__":'

class MainApplication():
    def __init__(self, AppName):
        self.AppName        = AppName
        self.tkFrameRoot    = tk.Tk()        
    # End of 'def __init__(self, parent):'

    def startApp(self):
        # Set App Title
        setTkFrameNameStatus = self.setTkFrameName(self.AppName)

        # Set App Frame size        

        print("Started")
        self.tkFrameRoot.mainloop()
    # End of 'def startApp(self):'

    def setTkFrameName(self, name):
        try:
            self._setTkFrameName(name)
            return True
        except Exception as setTkFrameNameError:
            print("setTkFrameNameError:", setTkFrameNameError)
            return False
        # End of 'try:'
    # End of 'def setTkFrameName(tkFrame, name):'

    def _setTkFrameName(self, name):
        self.tkFrameRoot.title(name)
    # End of 'def _setTkFrameName(self, name):'

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
