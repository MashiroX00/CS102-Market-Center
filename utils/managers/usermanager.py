from Config import *
# User Format Username | Password | Role
def insertUser(username:str,password:str,userrole:str,isAdmin: bool) -> bool:
    if isAdmin:
        try:
            stream = open(os.path.join(userStoragePath,"users.txt"),"a")
            stream.write(f"{username}\t{password}\t{userrole}\n")
            return True
        except:
            print("Insert User Failed")
            return False
    else:
        return False
def userReader() -> list:
    try:
        stream = open(os.path.join(userStoragePath,"users.txt"),"r")
        users = stream.read().splitlines()
        return users
    except:
        print("Read User Failed or file not found")
    return []

def removeUser(username:str) -> bool:
    users = userReader()
    removed = False
    try:
        stream = open(os.path.join(userStoragePath,"users.txt"),"w")
        for user in users:
            if user.split()[0] != username:
                stream.write(f"{user}\n")
            else:
                removed = True
        return removed
    except:
        print("Remove User Failed")
    return False

def resetPassword(username:str,password:str):
    users = userReader()
    try:
        stream = open(os.path.join(userStoragePath,"users.txt"),"w")
        for user in users:
            if user.split()[0] == username:
                user = user.split()
                user[1] = password
                user = " ".join(user)
            stream.write(f"{user}\n")
    except:
        print("Reset Password Failed")
    return False

