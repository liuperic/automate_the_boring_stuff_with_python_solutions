#!/usr/bin/env python3

# mistakes.py - Finds error in spreadsheet
# View spreadsheet here: https://docs.google.com/spreadsheets/d/1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg/edit?usp=sharing/

import ezsheets

ss = ezsheets.Spreadsheet('1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg')

# Iterate through all rows
rows = ss[0].getRows()
for row_num, i in enumerate(rows, 1):
    # Ensures cells are not empty
    if row_num > 1 and i[0] and i[1] and i[2]:
        # Print out row error calc is found in
        if int(i[0]) * int(i[1]) != int(i[2]):
            print(f'Error in calculation found on row: {str(row_num)}')
