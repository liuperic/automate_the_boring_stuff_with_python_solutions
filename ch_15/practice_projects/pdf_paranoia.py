#!/usr/bin/env python3
# Encrypts all PDF files in a directory (and its subfolders)

import os, PyPDF2, sys

if len(sys.argv) != 2:
    print('Usage Error: Incorrect number of command line arguments.\nPlease provide password to encrypt all PDF files with.')
    sys.exit(1)

pwd = sys.argv[1]

file_path = input('Please provide file path to the directory where PDF files will be encrypted: ')

# # Ask user if they would like to delete old pdf
# response = pyip.inputYesNo('Would you like to delete the unencrypted PDF files after they have been encrypted? (yes/no): ')

# Encrypts all PDFs with a password provided at command line.
for foldername, subfolders, filenames in os.walk(file_path):
    for filename in filenames:
        if filename.endswith('.pdf'):
            # Create path and new name of encrypted PDF file
            encrypt_name = foldername + '/' + filename.rstrip('.pdf') + '_encrypted.pdf'

            # Open PDF file and read 
            pdf_file = open(foldername + '/' + filename, 'rb')

            # Can only encrypt decrypted files
            pdf_reader = PyPDF2.PdfFileReader(pdf_file)
            if pdf_reader.isEncrypted:
                continue
            
            # Good to write if not encrypted
            pdf_writer = PyPDF2.PdfFileWriter()

            # Copy all pages of PDF into new file.
            for page_num in range(pdf_reader.numPages):
                pdf_writer.addPage(pdf_reader.getPage(page_num))
            
            # Encrypt PDF with password provided and save as new file
            pdf_writer.encrypt(pwd)
            result_pdf = open(encrypt_name, 'wb')
            pdf_writer.write(result_pdf)
            print(f'{filename} has been encrypted')

            result_pdf.close()

# Ensure all encrypted files can be open
for foldername, subfolders, filenames in os.walk(file_path):
    for filename in filenames:
        if filename.endswith('_encrypted.pdf'):
            encrypted_file = open(foldername + '/' + filename, 'rb')
            reader = PyPDF2.PdfFileReader(encrypted_file)
            if reader.isEncrypted:
                reader.decrypt(pwd)
                # Run test to make sure pdf is able to be read
                try:
                    # Will throw exception if cannot be read
                    reader.numPages
                except:
                    print(f'{filename} could not be opened')
                    continue

                # Delete original unencrypted file if encryption successful.
                original = foldername + '/' + filename.rstrip('_encrypted.pdf') + '.pdf'
                if os.path.isfile(original):
                    os.remove(original)
