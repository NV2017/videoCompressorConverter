# getGlobalVariables.py

# from imports import *

import os

osSeparator = os.path.sep

codesFolderName = 'Codes'
inputFolderName = 'Input'
outputFolderName = 'Output'
logFolderName = 'Log'
ErrorFolderName = 'Error'

mainCodesFolderPath = os.path.join(os.getcwd(),codesFolderName)

mainFolderPath = osSeparator.join(mainCodesFolderPath.split(osSeparator)[0:-1])

inputFolderPath = os.path.join(mainFolderPath,inputFolderName)
outputFolderPath = os.path.join(mainFolderPath,outputFolderName)
logFolderPath = os.path.join(mainFolderPath,logFolderName)
errorFolderPath = os.path.join(mainFolderPath,ErrorFolderName)