def inv_check(inventory: dict[str,int],demand:dict[str,int]):
    shortitem={}
    for key in demand:
        if key not in inventory:
            print("Not Present",key)
            continue
        if inventory[key]>=demand[key]:
            inventory[key]-=demand[key]
        elif inventory[key]<demand[key]:
            shortitem[key]=demand[key]-inventory[key]
            del inventory[key]
    return inventory,shortitem

inv={}
demands={}
n1=int(input("Enter number of terms : "))
for i in range(n1):
    key=input("Enter item : ")
    val=int(input("Enter quantity : "))
    inv[key]=val

n2=int(input("Enter number of terms : "))
for i in range(n2):
    key=input("Enter item : ")
    val=int(input("Enter quantity : "))
    demands[key]=val

invs,shortitem = inv_check(inv,demands)
print("inventory = ",invs)
print("Short item = ",shortitem)