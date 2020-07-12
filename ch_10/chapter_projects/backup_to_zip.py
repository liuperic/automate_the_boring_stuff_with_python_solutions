#!/usr/bin/env python3
# backup_to_zip.py - Copies an entire folder and its conents into
# a zip file whose filename increments.

import zipfile, os, pathlib

def backup_to_zip(folder):
    # Back up the entire contents of "folder" into a ZIP file.

    folder = os.path.abspath(folder)    # Make sure folder is absolute

    # Figure out the filename this code should use based on
    # what files already exist.
    number =  1
    while True:
        zip_filename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zip_filename):
            break
        number += 1

    print(f'Creating {zip_filename}...')
    backup_zip = zipfile.ZipFile(zip_filename, 'w') 

    # Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print(f'Adding files in {foldername}...')
        # Add the current folder to the ZIP file.
        backup_zip.write(foldername)

        # Add all the files in this folder to the zip file.
        for filename in filenames:
            new_base = os.path.basename(folder) + '_'
            if filename.startswith(new_base) and filename.endswith('.zip'):
                continue    # don't back up the backup ZIP files
            backup_zip.write(os.path.join(foldername, filename))
    backup_zip.close()
    print('Done')
