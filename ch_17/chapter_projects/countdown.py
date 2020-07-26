#!/usr/bin/env python3
# countdown.py - A simple countdown script.

import time, subprocess

time_left = 60
while time_left > 0:
    print(time_left, end='')
    time.sleep(1)
    time_left = time_left - 1
print()

# At the end of countdown, play a sound file.
subprocess.Popen(['open', 'alarm.wav'])  # For Mac OSX

# For Windows, use the following to play sound:
# subprocess.Popen(['start', 'alarm.wav', shell=True])


