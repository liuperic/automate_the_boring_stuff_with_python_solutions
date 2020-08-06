#!/usr/bin/env python3
# instant_messenger_bot.py - Sends message to Google Hangout contacts

import time
import pyautogui


def auto_message(name, message):
    """Searches for friends on Google Hangouts and messages them."""
    print('Make sure Google Hangouts is active tab. '
    'Looking for the message button on Google Hangouts web...')
    time.sleep(3)
    # Makes sure not on active conversation
    pyautogui.press('esc')

    # Web shortcut. keys 'hq' opens search bar
    pyautogui.write(['h', 'q'])
    pyautogui.press('enter')
    pyautogui.typewrite(name, 0.25)
    pyautogui.press('enter')

    pyautogui.typewrite(message, 0.25)
    # Gives user time to check if contact is correct.
    time.sleep(2)
    pyautogui.press('enter')
    print('Message sent to ' + name)


print('Please enter the contacts you would like to send as message to (i.e., Eric, Dave, Bryant)')
contacts = input().split(', ')
contents = input('What message would you like to send?\n')

for contact in contacts:
    auto_message(contact, contents)