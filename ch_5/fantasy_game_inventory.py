def display_inventory(inventory):
    print('Inventory:')
    total_items = 0
    for k, v in inventory.items():
        print(str(v), k)
        total_items += v
    print()
    print('Total number of items:', total_items)

def add_to_inventory(inventory, added_items):
    for item in added_items:
        inventory.setdefault(str(item), 0)
        inventory[item] += 1
    return inventory


inv = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)
