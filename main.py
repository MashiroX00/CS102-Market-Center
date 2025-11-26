from utils.checkingfile import isFileExists
import os
from Config import *
from src.welcomeUI.rookie import welcomerookie
from src.mainscreen.mainscreen import mainScreen
from src.mainscreen.loginscreen import Login
session = []
## Config

# checking 
isUsersFileExists = isFileExists(userStoragePath,"users.txt")
isItemsFileExists = isFileExists(itemStoragePath,"items.txt")

if not isUsersFileExists:
    welcomerookie()
else:
    if session:
        mainScreen(session=session)
    else:
        while True:
            session = Login()
            if session:
                mainScreen(session=session)
                break
            else:
                print("Login Failed")
                continue

        