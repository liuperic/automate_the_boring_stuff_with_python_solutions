#!/usr/bin/env python3

def display_inventory(inventory):
    print('Inventory:')
    total_items = 0
    for k, v in inventory.items():
        print(str(v), k)
        total_items += v
    print('Total number of items:', total_items)

def add_to_inventory(inventory, added_items):
    for item in added_items:
        inventory.setdefault(str(item), 0)
        inventory[item] += 1
    return inventory


inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
display_inventory(inv) 