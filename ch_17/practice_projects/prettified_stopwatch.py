#!/usr/bin/env python3
# prettified_stopwatch.py - A prettified version of the stopwatch program
# Copies each lap to clipboard.

import time, pyperclip

# Display the program's instructions.
print('Press ENTER to begin. Afterward, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
input()     # press Enter to begin
print('Started.')
start_time = time.time() # Get the first lap's start time
last_time = start_time
lap_num = 1

# Start tracking the lap times.
try:
    while True:
        input()
        lap_time = round(time.time() - last_time, 2)
        total_time = round(time.time() - start_time, 2)
        lap = f'lap # {(str(lap_num) + ":").ljust(3)} {str(total_time).rjust(5)} ({str(lap_time).rjust(6)})'
        print(lap, end='')
        lap_num += 1
        last_time = time.time() # reset the last lap time
        pyperclip.copy(lap)
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone.')
