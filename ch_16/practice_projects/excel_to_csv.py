#!/usr/bin/env python3
# excel_to_csv.py - Reads all Excel files in current working directory
# and outputs them as CSV files.

import os, csv, openpyxl

for excel_file in os.listdir('.'):
    # Skip non-xlsx files, load the workbook object.
    if not excel_file.endswith('.xlsx'):
        continue

    wb = openpyxl.load_workbook(excel_file)

    for sheet_name in wb.sheetnames:
        # Loop through every sheet in the workbook.
        sheet = wb[sheet_name]

        # Create the CSV filename from the Excel filename and sheet title.
        csv_filename = excel_file.rstrip('.xlsx') + '_' + sheet_name + '.csv'
        # Create the csv.writer object for this CSV file.
        csv_file = open(csv_filename, 'w', newline='')
        csv_writer = csv.writer(csv_file)

        # Loop through every row in the sheet.
        for row_num in range(1, sheet.max_row + 1):
            row_data = []    # append each cell to this list
            # Loop through each cell in the row.
            for col_num in range(1, sheet.max_column + 1):
                # Append each cell's data to rowData.
                row_data.append(sheet.cell(row=row_num, column=col_num).value)
            # Write the rowData list to the CSV file.
            csv_writer.writerow(row_data)
        csv_file.close()