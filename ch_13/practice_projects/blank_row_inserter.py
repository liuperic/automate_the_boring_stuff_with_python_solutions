#!/usr/bin/env python3
# blank_row_inserter - Inserts blank rows into excel file

"""Usage: python blank_row_inserter.py <row to insert blank rows> <number of blank rows> <file name>"""

import openpyxl, sys

insert_before_row = int(sys.argv[1])
num_of_rows = int(sys.argv[2])
file_name = sys.argv[3]

wb = openpyxl.load_workbook(file_name)
sheet = wb.active
sheet.insert_rows(insert_before_row, num_of_rows)   # Insert number of rows
wb.save(file_name)   # WARNING: Will overwrite original file