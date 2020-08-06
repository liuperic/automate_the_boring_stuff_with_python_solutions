#/usr/bin/env python3
# looking_busy.py - Moves mouse to avoid idle status.

import time
import pyautogui

print('Press CTRL-C to quit.')
try:
    while True:
        pyautogui.move(5, 0, 0.25)
        pyautogui.move(-5, 0, 0.25)
        time.sleep(10)
except KeyboardInterrupt:
    print('Program exited.')