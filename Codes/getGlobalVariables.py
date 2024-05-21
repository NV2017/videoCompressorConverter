# getGlobalVariables.py

# from imports import *

import os

osSeparator = os.path.sep

inputFolderName = 'Input'
outputFolderName = 'Output'
codesFolderName = 'Codes'

mainCodesFolderPath = os.path.join(os.getcwd(),codesFolderName)

mainFolderPath = osSeparator.join(mainCodesFolderPath.split(osSeparator)[0:-1])

inputFolderPath = os.path.join(mainFolderPath,inputFolderName)
outputFolderPath = os.path.join(mainFolderPath,outputFolderName)