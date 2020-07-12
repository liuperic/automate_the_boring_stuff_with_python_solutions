#!/usr/bin/env python3

import os, shutil
from pathlib import Path

def large_files(folder):
    """large_files prints out all files or folders in a folder tree with a file size over 100MB

    Args:
        folder (string): file path of directory
    """
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            target_file = foldername + '/' + filename
            if os.path.getsize(target_file) > 100000000:    # 100000000 = 100MB
                print(f'{target_file}: {str(os.path.getsize(target_file))} bytes')

if __name__ == '__main__':
    target_dir = input('Please enter the directory you would like to search for large files: ')
    large_files(target_dir)



