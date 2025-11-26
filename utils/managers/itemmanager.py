from Config import *
# Item Format ID | ItemName | price 
def itemReader() -> list:
    try:
        stream = open(os.path.join(itemStoragePath,"items.txt"),"r")
        items = stream.read().splitlines()
        return items
    except:
        print("Read Item Failed or file not found")
    return []


def insertItem(itemname:str,itemprice:str) -> bool:
    try:
        items = itemReader()
        stream = open(os.path.join(itemStoragePath,"items.txt"),"a")
        id = 0
        if items:
            id = int(items[-1].split()[0]) + 1
        stream.write(f"{id}\t{itemname}\t{itemprice}\n")
        return True
    except:
        print("Insert Item Failed")
    return True

def removeItem(itemid:str) -> bool:
    items = itemReader()
    removed = False
    try:
        stream = open(os.path.join(itemStoragePath,"items.txt"),"w")
        for item in items:
            if item.split()[0] != itemid:
                stream.write(f"{item}\n")
            else:
                removed = True
        return removed
    except:
        print("Remove Item Failed")
    return False

# Format | Discount_Id | Code | percent | maximum
def discountReader() -> list:
    try:
        stream = open(os.path.join(itemStoragePath,"discount.txt"),"r")
        discounts = stream.read().splitlines()
        return discounts
    except:
        print("Read Discount Failed or file not found")
    return []

def insertDiscount(code:str,percent:str,maximum:str) -> bool:
    try:
        discount = discountReader()
        stream = open(os.path.join(itemStoragePath,"discount.txt"),"a")
        id = 0
        if discount:
            id = int(discount[-1].split()[0]) + 1
        stream.write(f"{id}\t{code}\t{percent}\t{maximum}\n")
        return True
    except:
        print("Insert Discount Failed")
    return True

def removeDiscount(discountId:str) -> bool:
    discounts = discountReader()
    removed = False
    try:
        stream = open(os.path.join(itemStoragePath,"discount.txt"),"w")
        for discount in discounts:
            if discount.split()[0] != discountId:
                stream.write(f"{discount}\n")
            else:
                removed = True
        return removed
    except:
        print("Remove Discount Failed")
    return False