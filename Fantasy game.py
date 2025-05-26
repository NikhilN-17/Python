#fantasygameinvetor 
print("Nikhil N,USN:1AY24AI075,SEC:O")

game_inventory = {'rope' : 1, 'gold coin' : 42}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory(inventory, addedItems):
    print('Inventory:')
    total = 0
    # Update existing items
    for k, v in inventory.items():
        if k in addedItems:
            o = addedItems.count(k)
            inventory[k] = v + o
    # Add new items
    for k2 in addedItems:
        if k2 not in inventory.keys():
            inventory[k2] = addedItems.count(k2)
    # Print inventory with new format
    for k3, v2 in inventory.items():
        print(f"- {k3}: {v2}")
        total += v2
    print(f"Total items count: {total}")

addToInventory(game_inventory, dragon_loot)

