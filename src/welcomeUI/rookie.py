from utils.managers.usermanager import insertUser
# fist run

def welcomerookie() -> bool:
    print("==="*20)
    print(f"{'Welcome to Market Center(First Setup)':^60}")
    print("==="*20)
    print("let's Create admin account!")
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    userrole = "admin"
    isAdmin = True
    insertUser(username,password,userrole,isAdmin)
    return True