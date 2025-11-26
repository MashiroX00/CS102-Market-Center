from utils.managers.sessionmanager import verfiedCredentials

def Login() -> list:
    print("==="*20)
    print(f"{'Login':^60}")
    print("==="*20)
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    isVerified = verfiedCredentials(username,password)
    if isVerified:
        return isVerified
    else:
        return []