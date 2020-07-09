#!/usr/bin/env python3
# Asks users for sandwich preferences

import pyinputplus as pyip

price_menu = {'wheat': 1.5, 'white': 1.25, 'sourdough': 1.75,
                'chicken': 3.25, 'turkey': 3.00, 'ham': 3.00, 'tofu': 3.5,
                'cheddar': .5, 'Swiss': .5, 'mozzarella': .5,
                'mayo': .25, 'mustard': .25, 'lettuce': .50, 'tomato': .50}   

preferences = []

preferences.append(pyip.inputMenu(['wheat', 'white', 'sourdough']))
preferences.append(pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu']))
preferences.append(pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella']))
if pyip.inputYesNo('mayo? (yes/no)\n') == 'yes':
    preferences.append('mayo')
if pyip.inputYesNo('mustard? (yes/no)\n') == 'yes':
    preferences.append('mustard')
if pyip.inputYesNo('lettuce? (yes/no)\n') == 'yes':
    preferences.append('lettuce')
if pyip.inputYesNo('tomato? (yes/no)\n') == 'yes':
    preferences.append('tomato')
num_sandwiches = pyip.inputInt('How many sandwiches would you like?\n', min=1)

total_price = 0
for item in preferences:
    total_price += price_menu[item]

print(f'Your total is ${total_price * num_sandwiches}')
