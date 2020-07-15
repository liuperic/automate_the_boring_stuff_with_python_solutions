#!/usr/bin/env python3
# command_line_emailer.py - Logs into email and sends string of text to email provided

import pyinputplus as pyip
import getpass, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

email = pyip.inputEmail('Enter your email address: ')   # Prompt user for their email address
pwd = getpass.getpass()

# Open and log into gmail
browser = webdriver.Firefox()
browser.get('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
user_elem = browser.find_element_by_id('identifierId')  # Specific to Gmail. Change for other emails
user_elem.send_keys(email)

# Find and click 'Next' button. Class name specific to Gmail
next_elem = browser.find_element_by_class_name('VfPpkd-RLmnJb')
next_elem.click()

time.sleep(1)   # Wait before looking for password element
pwd_elem = browser.find_element_by_name('password')
pwd_elem.send_keys(pwd)

# Find and click 'Next' button. Class name specific to Gmail
next_elem = browser.find_element_by_class_name('VfPpkd-RLmnJb')
next_elem.click()

# Get email content and email to send to
recipient = pyip.inputEmail('What is the email address you would like to send an email to?\n')
subject = pyip.inputStr('Enter the tile of the email subject.\n')
contents = pyip.inputStr('Enter the email you would like to send.\n')
time.sleep(2)   # Wait before looking for compose element

# Click on compose email button
compose_elem = browser.find_element_by_class_name('z0')
compose_elem.click()
time.sleep(5)

# Type recipient
to_elem = browser.find_element_by_name('to')
to_elem.send_keys(recipient)

# Type subject
subject_elem = browser.find_element_by_name('subjectbox')
subject_elem.send_keys(subject)

# Type and send contents
subject_elem.send_keys(Keys.TAB + contents + Keys.TAB + Keys.ENTER)
