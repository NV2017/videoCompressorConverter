# pureTkGUIfunctions.property

class pureTkGUIfunctions():
    def _setTkFrameName(tkFrameRoot, name):
        tkFrameRoot.title(name)
    # End of 'def _setTkFrameName(self, name):'

    def _setTkAppWindowSize(tkFrameRoot, width, height):
        tkFrameRoot.geometry('{0}x{1}'.format(width,height))
    # End of 'def _setTkAppWindowSize(tkFrameRoot, width, height):'
# End of 'class pureTkGUIfunctions():'