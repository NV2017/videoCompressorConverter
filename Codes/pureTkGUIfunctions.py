# pureTkGUIfunctions.property

from imports import *

class pureTkGUIfunctions():
    def _setTkFrameName(tkFrameRoot, name):
        tkFrameRoot.title(name)
    # End of 'def _setTkFrameName(self, name):'

    def _setTkAppWindowSize(tkFrameRoot, width, height):
        tkFrameRoot.geometry('{0}x{1}'.format(width,height))
    # End of 'def _setTkAppWindowSize(tkFrameRoot, width, height):'

    def _menuBarButtonsSwitchCreate(tkFrameRoot     = None,
                                    MenuBar         = None,
                                    ButtonsList     = None, 
                                    FileStr         = getGlobalVariables.GUIfileButtonStr,
                                    FolderStr       = getGlobalVariables.GUIfolderButtonStr,
                                    ThemeStr        = getGlobalVariables.GUIthemeButtonStr,
                                    ExitStr         = getGlobalVariables.GUIexitButtonStr,
                                    ThemeOptions    = getGlobalVariables.GUIthemeButtonOptions):

        for buttonItem in ButtonsList:
            print("buttonItem:", buttonItem)
            if buttonItem == FileStr:
                # Create a Cascade Menu
                fileMenu = Menu(MenuBar)
                fileMenu = Menu(fileMenu, tearoff=False)

                # Add a menu item to the cascade
                fileMenu.add_command(label=ExitStr, command=tkFrameRoot.destroy)

                # Add the File menu to the cascade
                MenuBar.add_cascade(label=FileStr, menu=fileMenu)
            # elif buttonItem == FolderStr:
                # FolderButton = MenuBar.add_command(label=FolderStr)
            elif buttonItem == ThemeStr:
                # Create a Cascade Menu
                themeMenu = Menu(MenuBar)
                themeMenu = Menu(themeMenu, tearoff=False)

                # Add a menu item to the cascade
                themeMenu.add_command(label=ThemeOptions[0], background='black', activebackground='darkgrey', activeforeground='white', foreground='white')
                themeMenu.add_command(label=ThemeOptions[1], background='white', activebackground='white', activeforeground='gray')

                # Add the File menu to the cascade
                MenuBar.add_cascade(label=ThemeStr, menu=themeMenu)

            # elif buttonItem == ExitStr:
            #     ExitButton = MenuBar.add_command(label=ExitStr, command=tkFrameRoot.destroy)
            else:
                print("?:")
        # End of 'for buttonItem in ButtonsList:'
    # End of 'def _menuBarButtonsSwitchCreate(ButtonsList = None):'

    def _addTkAppMenuBar(tkFrameRoot, MenuBar, Buttons):
        # Create a Menubar
        tkFrameRoot.config(menu=MenuBar)

        # Give function to the buttons
        pureTkGUIfunctions._menuBarButtonsSwitchCreate(tkFrameRoot = tkFrameRoot, MenuBar = MenuBar, ButtonsList = Buttons)

        print("Hello from: {0}".format(__name__))
    # End of 'def addTkAppMenuBar(tkFrameRoot):'
# End of 'class pureTkGUIfunctions():'