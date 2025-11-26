import os
import platform

def clearscreen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")