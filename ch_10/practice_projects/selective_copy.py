#!/usr/bin/env python3

import os, shutil
from pathlib import Path

def selective_copy(folder, copy_folder):
    """selective_copy copies all jpg and pdf files to specified folder

    Args:
        folder (string): file path of directory to be copied from
        copy_folder (string): file path of directory for files to be copied over to
    """
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            if filename.endswith('.pdf') or filename.endswith('.jpg'):
                target_file = foldername + '/' + filename
                if os.path.isfile(copy_folder + '/' + filename):
                    print(f'Oops! Looks like there is already a file named {filename} in the copy folder. File: {target_file} was not copied over.')
                    continue
                shutil.copy(target_file, copy_folder)

if __name__ == '__main__':
    target_dir = input('Please enter the directory you would like to copy jpg and pdf files from: ')
    copy_folder = input('Please enter the directory in which you would like the copied files to be saved in: ')
    selective_copy(target_dir, copy_folder)



