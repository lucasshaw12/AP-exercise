# Write a function that displays the inventory

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print('Inventory')
    item_total = 0
    for k, v in inventory.items():
        print(v, k)
    item_total = sum(inventory.values())
    print('Total number of items: ' + str(item_total))

displayInventory(stuff) 

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inv.setdefault(item, 0)
        inv[item] = inv[item] + 1
    return inv 

        


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)

displayInventory(inv)