
def mainmenu(role: str) -> str:
    print("1) Seller program\n2) Add Items\n3) Remove Items\n4) List All Item\n5) Exit")
    if role == "admin":
        print("6) Add User\n7) Remove User\n8) List All User\n9) Reset Password")
    print("==="*20)
    menu = input("Choose Menu: ")
    print("==="*20)
    return menu