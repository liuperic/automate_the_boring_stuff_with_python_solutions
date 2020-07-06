#!/usr/bin/env python3

# List to Dictionary function for fantasy game inventory.
# Can now add list to inventory and display updated inventory thereafter.

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


inv = {'rope': 1, 'gold coin': 42}
display_inventory(inv)  # Print inventory list pre-dragon loot
print()
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)  # Print inventory list post-dragon loot
