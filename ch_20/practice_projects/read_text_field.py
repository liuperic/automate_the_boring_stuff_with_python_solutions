#/usr/bin/env python3
# read_text_field.py - Obtain window for Notepad and copy to clipboard text.

import pyperclip
import pyautogui

# Find notepad window and ensure it is active
window = pyautogui.getWindowsWithTitle('Notepad')
notepad = window[0]
notepad.activate()

# Find location of window
notepad_pos = notepad.topleft
pyautogui.moveTo(notepad_pos)

# Move to editable text area.
pyautogui.move(100, 200)
pyautogui.click()

pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')

text = pyperclip.paste()
# Print contents
print(text)