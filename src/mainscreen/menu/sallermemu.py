from utils.managers.itemmanager import *
from utils.clearscreen import clearscreen

def sallermenu():
    print("==="*20)
    print(f"{'Welcome to Saller Program':^60}")
    print("==="*20)
    while True:
        print("1) Checkout\n2) Add Discount\n3) Remove Discount\n4) List All Discount\n5) Exit")
        print("==="*20)
        menu = input("Choose Menu: ")
        print("==="*20)
        if menu == "1":
            itemids = []
            itemprices = []
            while True:
                clearscreen()
                itemid = input("Enter Item ID: ")
                itemids.append(itemid)
                isexit = input("Checkout? (Y/N): ")
                if isexit.lower() == "y":
                    break
            for itemid in itemids:
                items = itemReader()
                for item in items:
                    if item.split()[0] == itemid:
                        itemprices.append(item.split()[2])
                        break
            totalprice = 0
            for price in itemprices:
                totalprice += float(price)
            print(f"Total Price: {totalprice}")
            print("==="*20)
            discountcode = input("Enter Discount Code: ")
            discounts = discountReader()
            for discount in discounts:
                if discount.split()[1] == discountcode:
                    totalprice -= float(discount.split()[2]) * totalprice / 100
                    if float(discount.split()[3]) < totalprice:
                        totalprice -= float(discount.split()[3])
                    break
            print(f"Total Price After Discount: {totalprice}")
            print("==="*20)
        elif menu == "2":
            clearscreen()
            code = input("Enter Discount Code: ")
            percent = input("Enter Discount Percent: ")
            maximum = input("Enter Discount Maximum: ")
            issucceded = insertDiscount(code=code,percent=percent,maximum=maximum)
            print("Add Discount Succeded" if issucceded else "Add Discount Failed")
            print("==="*20)
        elif menu == "3":
            clearscreen()
            id = input("Enter Discount ID: ")
            issucceded = removeDiscount(discountId=id)
            print("Remove Discount Succeded" if issucceded else "Remove Discount Failed or Discount not found")
            print("==="*20)
        elif menu == "4":
            clearscreen()
            discounts = discountReader()
            print(f"{'Discount List':^60}")
            print("==="*20)
            print(f"{'Discount ID':<20}{'Code':<20}{'Percent':<20}{'Maximum':<20}")
            print(f"{'========':<20}{'=====':<20}{'=====':<20}{'======':<20}")
            for discount in discounts:
                print(f"{discount.split()[0]:<20}{discount.split()[1]:<20}{discount.split()[2]:<20}{discount.split()[3]:<20}")
                print("==="*20)
        elif menu == "5":
            clearscreen()
            print("Good bye!")
            break
        else:
            print("Invalid Menu")
            print("==="*20)
            continue
    print("==="*20)