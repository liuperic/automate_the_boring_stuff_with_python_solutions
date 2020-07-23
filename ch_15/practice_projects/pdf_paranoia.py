#!/usr/bin/env python3
# Encrypts all PDF files in a directory (and its subfolders)

import os, PyPDF2, sys

if len(sys.argv) != 2:
    print('Usage Error: Incorrect number of command line arguments.\nPlease provide password to encrypt all PDF files with.')
    sys.exit(1)

pwd = sys.argv[1]

file_path = input('Please provide file path to the directory where PDF files will be encrypted: ')

# Encrypts all PDFs with a password provided at command line.
for foldername, subfolders, filenames in os.walk(file_path):
    for filename in filenames:
#         target_file = foldername + '/' + filename

# Saves encrypted PDFs in new file, test to validate encryption works
# Then delete oriiginal unencrypted file.



# Finds all encrypted PDFs in a folder (and subfolders).
# Creates a decrypted copy of PDF using provided password
# If password is incorrect, program should print message to user