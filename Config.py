import os

rootpath = os.path.dirname(os.path.realpath(__file__))
storagepath = os.path.join(rootpath, "localStorage")
userStoragePath = os.path.join(storagepath,"users")
itemStoragePath = os.path.join(storagepath,"items")