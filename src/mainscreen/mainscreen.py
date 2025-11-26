from src.mainscreen.menu.mainmenu import mainmenu
from utils.managers.itemmanager import *
from utils.managers.usermanager import *
from utils.clearscreen import clearscreen
from src.mainscreen.menu.sallermemu import *

def mainScreen(session: list):
    clearscreen()
    print("==="*20)
    print(f"{'Welcome to Market Center':^60}")
    print("==="*20)
    print(f"Logged in as {session[0]}#{session[2]}")
    while True:
        menu = mainmenu(session[2])
        if menu == "5":
            print("Good bye!")
            break
        elif menu == "1":
            sallermenu()
            print("==="*20)
        elif menu == "2":
            clearscreen()
            itemname = input("Enter Item Name: ")
            itemprice = input("Enter Item Price: ")
            issucceded = insertItem(itemname=itemname,itemprice=itemprice)
            print("Add Item Succeded" if issucceded else "Add Item Failed")
            print("==="*20)
        elif menu == "3":
            clearscreen()
            id = input("Enter Item ID: ")
            issucceded = removeItem(itemid=id)
            print("Remove Item Succeded" if issucceded else "Remove Item Failed or Item not found")
            print("==="*20)
        elif menu == "4":
            clearscreen()
            items = itemReader()
            print(f"{'Item List':^60}")
            print("==="*20)
            print(f"{'ID':<20}{'Item Name':<20}{'Price':<20}")
            print(f"{'==':<20}{'=========':<20}{'=====':<20}")
            for item in items:
                print(f"{item.split()[0]:<20}{item.split()[1]:<20}{item.split()[2]:<20}")
            print("==="*20)
        elif menu == "6" and session[2] == "admin":
            clearscreen()
            role = ["admin","user"]
            while True:
                userName = input("Enter Username: ")
                UserPass = input("Enter Password: ")
                userrole = input("Enter User Role(1 = admin/2 = user): ")
                if userrole == "1":
                    userrole = role[0]
                elif userrole == "2":
                    userrole = role[1]
                else:
                    print("Invalid Role")
                    break
                issucceded = insertUser(username=userName,password=UserPass,userrole=userrole,isAdmin=True)
                print("Add User Succeded" if issucceded else "Add User Failed")
                print("==="*20)
                break
        elif menu == "7" and session[2] == "admin":
            clearscreen()
            username = input("Enter Username: ")
            issucceded = removeUser(username=username)
            print("Remove User Succeded" if issucceded else "Remove User Failed or User not found")
            print("==="*20)
        elif menu == "8" and session[2] == "admin":
            clearscreen()
            users = userReader()
            print(f"{'User List':^60}")
            print("==="*20)
            print(f"{'Username':<20}{'Role':<20}")
            print(f"{'========':<20}{'====':<20}")
            for user in users:
                print(f"{user.split()[0]:<20}{user.split()[2]:<20}")
            print("==="*20)
        elif menu == "9" and session[2] == "admin":
            clearscreen()
            username = input("Enter Username: ")
            password = input("Enter New Password: ")
            issucceded = resetPassword(username=username,password=password)
            print("Reset Password Succeded" if issucceded else "Reset Password Failed or User not found")
            print("==="*20)
            continue
        else:
            clearscreen()
            print("Invalid Menu")
            print("==="*20)
            continue