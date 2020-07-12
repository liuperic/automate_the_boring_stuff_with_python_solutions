#!/usr/bin/env python3

import os, re, shutil

def fill_in_gaps(folder, prefix):
    """fill_in_gaps: given a prefix, finds all file in a single folder and locates any gaps in
    numbering and renames all later files to fill gap.

    Args:
        folder (string): directory path to be searched in
        prefix (string): prefix name of files
    Returns:
        None
    
    Usage: If files are spam001.txt, spam003.txt,... and so forth, 
    would rename spam003.txt and all later files to spam002.txt and so forth.
    """
    numbering_regex = re.compile(rf'({prefix})(\d*)(.*)(\..*)')
    
    # List of filename matches
    match = []  

    for filename in os.listdir(folder):
        if numbering_regex.search(filename):
            num_length = int(len(numbering_regex.search(filename).group(2)))   # Length of number naming digits
            suffix = numbering_regex.search(filename).group(4)
            match.append(numbering_regex.search(filename).group(2))
        ordered = sorted(int(i) for i in match)

    for number in range(1, len(match) + 1):
        zeroes = '0' * (num_length - len(str(number)))   # Number of zeroes in numbering of file

        # File path of current file
        current_file = f'{folder}/{prefix}{zeroes}{number}{suffix}'

        # Start renumbering and renaming if file does not already exist
        if not os.path.exists(current_file):
            # Numbering of old file name
            old_num = ordered[number - 1]
            old_zeroes = '0' * (num_length - len(str(old_num)))
            # Name and file path of old file
            old_file = (folder + '/' + prefix + str(old_zeroes) + str(old_num) + suffix)
            # Update numbering of file name
            shutil.move(old_file, current_file)

if __name__ == '__main__':
    folder = input("Enter a file path: ")
    prefix = input("Enter the prefix of the files to be checked: ")
    fill_in_gaps(folder, prefix)

