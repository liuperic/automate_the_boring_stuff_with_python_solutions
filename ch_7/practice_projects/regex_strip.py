#!/usr/bin/env python3

import re

# Regex version of strip()
def regex_strip(string, rm_str=None):
    """ Strips white space at beginning and end of string if no second optional argument is given.
    If optional argument given, strip second string argument from beginning and end of first argument string.
    """
    if rm_str:
        return re.compile(rf'^({rm_str})*|({rm_str})*$').sub('', string)
    else:
        return re.compile(r'^(\s)*|(\s)*$').sub('', string)


if __name__ == '__main__':
    string1 = 'hey! stop saying hey'
    string2 = '  delete the white spaces please?   '
    substring = 'hey'
    print(regex_strip(string1, substring))  # => '! stop saying '
    print(regex_strip(string2)) # => 'delete the white spaces please?'
