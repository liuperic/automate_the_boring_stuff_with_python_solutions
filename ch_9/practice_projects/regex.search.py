#!/usr/bin/env python3

import re, pathlib, os

def regex_search(folder_path, regex):
    """regex_search Opens all .txt files in a folder and searches for any string that matches a user-supplied regular expressions.

    Args:
        path ([string]): [Directory path string]        
        regex ([string]): [Regular expression to be searched for in .txt files]
    Returns:
        None
    Usage: Provide a regular expression to be searched for. Example: regex_search('.', '*')
        Will print out lines in all .txt files that matches the regular expression parameter.
    """
    user_regex = re.compile(regex)

    if not os.path.isdir(folder_path):
        print('Please enter a valid folder_path')
        return

    for file_name in os.listdir(folder_path):

        if file_name.endswith('.txt'):
            with open(file_name) as file:
                for line in file:
                    if user_regex.search(line): print(line, end='')


if __name__ == "__main__":

    regex = input('Please enter a regular expression to be searched for in .txt files: ')
    regex_search('.', regex)

