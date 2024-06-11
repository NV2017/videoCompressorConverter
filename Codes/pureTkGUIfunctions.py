# pureTkGUIfunctions.property

from imports import *

class pureTkGUIfunctions():
    def _setTkFrameName(tkFrameRoot, name):
        tkFrameRoot.title(name)
    # End of 'def _setTkFrameName(self, name):'

    def _setTkAppWindowSize(tkFrameRoot, width, height):
        tkFrameRoot.geometry('{0}x{1}'.format(width,height))
    # End of 'def _setTkAppWindowSize(tkFrameRoot, width, height):'

    def _menuBarButtonsSwitchCreate(tkFrameRoot = None,
                                    MenuBar     = None,
                                    ButtonsList = None, 
                                    FileStr     = getGlobalVariables.GUIfileButtonStr,
                                    FolderStr   = getGlobalVariables.GUIfolderButtonStr,
                                    DarkStr     = getGlobalVariables.GUIdarkButtonStr,
                                    LightStr    = getGlobalVariables.GUIlightButtonStr,
                                    ExitStr     = getGlobalVariables.GUIexitButtonStr):
        for buttonItem in ButtonsList:
            print("buttonItem:", buttonItem)
            if buttonItem == FileStr:
                print("FileStr:", FileStr)
            elif buttonItem == FolderStr:
                print("FolderStr:", FolderStr)
            elif buttonItem == DarkStr:
                print("DarkStr:", DarkStr)
            elif buttonItem == LightStr:
                print("LightStr:", LightStr)
            elif buttonItem == ExitStr:
                print("ExitStr:", ExitStr)
                ExitButton = MenuBar.add_command(label=ExitStr, command=tkFrameRoot.destroy)
            else:
                print("?:")
        # End of 'for buttonItem in ButtonsList:'
    # End of 'def _menuBarButtonsSwitchCreate(ButtonsList = None):'

    def _addTkAppMenuBar(tkFrameRoot, MenuBar, Buttons):
        # Create a Menubar
        tkFrameRoot.config(menu=MenuBar)

        # Iterate over buttons
        pureTkGUIfunctions._menuBarButtonsSwitchCreate(tkFrameRoot = tkFrameRoot, MenuBar = MenuBar, ButtonsList = Buttons)

        print("Hello from: {0}".format(__name__))
    # End of 'def addTkAppMenuBar(tkFrameRoot):'
# End of 'class pureTkGUIfunctions():'