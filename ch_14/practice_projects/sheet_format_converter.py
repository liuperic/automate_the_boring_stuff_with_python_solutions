#!/usr/bin/env python3

"""Converts Google Spreadsheet into other formats."""
import ezsheets, os

excel_file = input('Enter the path to the excel file you would like to upload to Google Sheets: ')
# Upload spreadsheet onto Google
ss = ezsheets.upload(excel_file)

# Create directory named after file without extension to store all converted formats
# Creates folder only if it does not already exist
file_name = os.path.basename(excel_file).rstrip('.xlsx')
try:
    os.mkdir(file_name)
except:
    pass

# Downloads Open Office, CSV, and PDF formats of the uploaded excel file into created directory
os.chdir(os.path.join(os.getcwd(), file_name))
ss.downloadAsODS()
ss.downloadAsCSV()
ss.downloadAsPDF()


