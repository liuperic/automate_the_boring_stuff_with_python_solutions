# #!/usr/bin/env python3

"""Tries to decrypt PDF file using every word in dictionary file as password guess"""

import os, PyPDF2

dictionary = []
file_name = input('Enter absolute path of PDF file')

# Add dictionary to a list (per book specs)
with open('dictionary.txt', 'r') as f:
    lines = f.readlines()

    # Add each word to dictionary list in both cases
    for line in lines:
        dictionary.append(line.strip())
        dictionary.append(line.strip().lower())


pdf_file = open(file_name, 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_file) 

solved = False
# Brute force password guessing
for word in dictionary:
    if pdf_reader.decrypt(word):
        print(f'Password to {file_name} is {word}')
        solved = True
        break

# Print files that could not be decrypted.
if solved == False:
    print(f'Could not decrypt {file_name}')

#Close file
pdf_file.close() 