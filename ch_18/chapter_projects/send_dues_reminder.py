#!/usr/bin/env python3
# send_dues_reminder - Sends email based on payment status in spreadsheet.

import getpass, openpyxl, smtplib, sys

import pyinputplus as pyip

my_email = pyip.inputEmail('Enter your email address: ')   
pwd = getpass.getpass()

# Open spreadsheet and get the latest dues status.

wb = openpyxl.load_workbook('duesRecords.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')
last_col = sheet.max_column
lastest_month = sheet.cell(row=1, column=last_col).value

# Check each member's payment status.
unpaid_members = {}
for r in range(2, sheet.max_row + 1):
    payment = sheet.cell(row=r, column=last_col).value
    if payment != 'paid':
        name = sheet.cell(row=r, column=1).value
        email = sheet.cell(row=r, column=2).value
        unpaid_members[name] = email

# Log in to email account
smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
smtp_obj.ehlo()
smtp_obj.starttls()
smtp_obj.login(my_email, pwd)

# Send out reminder emails.
for name, email in unpaid_members.items():
    body = 'Subject: %s dues unpaid.\nDear %s, \nRecords show that you have not paid dues for %s. Please make this payment as soon as possible. Thank you!' % (lastest_month, name, lastest_month)
    print('Sending email to %s...' % email)
    send_mail_status = smtp_obj.sendmail(my_email, email, body)
    if send_mail_status != {}:
        print('There was a problem sending email to %s: %s' % (email, send_mail_status))
smtp_obj.quit()