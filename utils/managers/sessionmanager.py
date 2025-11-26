from Config import *
def verfiedCredentials(username:str,password:str) -> list:
    try:
        stream = open(os.path.join(userStoragePath,"users.txt"),"r")
        users = stream.read().splitlines()
        for user in users:
            user = user.split()
            if user[0] == username and user[1] == password:
                return user
        return []
    except:
        print("Failed  to verify credentials")
