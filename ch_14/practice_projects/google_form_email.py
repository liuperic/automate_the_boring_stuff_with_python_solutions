#!/usr/bin/env python3
# google_form_email.py - Collects and prints list of email addresses
# from google spreadsheet derived from google form data.

import ezsheets, re

google_sheet = input('Please enter the url or unique id of the Google Spreadsheet: ')

# Email regular expression
email_regex = re.compile(r'.*?\s?(email address).*?', re.I)

# Loading Google Spreadsheet
ss = ezsheets.Spreadsheet(google_sheet)
sheet = ss[0]

# Get list of data for first row (headers)
header_row = sheet.getRows()[0]

# Look for email address header, column index for sheets starts at index 1.
for count, header in enumerate(header_row, 1):
    if email_regex.search(header) != None:
        # Store index column of email header
        email_index = count

email_column = sheet.getColumn(email_index)[1:]     # Ignore email header
# Don't store any blank rows
email_list = []
for email in email_column:
    if email != '':
        email_list.append(email)
# Print list of email list
print(email_list)