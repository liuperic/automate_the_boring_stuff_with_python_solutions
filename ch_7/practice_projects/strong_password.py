#!/usr/bin/env python3

import re

def strong_password(password):
    """Determines whether a password meets the strong requirements.

    Args:
        password: A string representing a password
    
    Returns:
        Boolean - True if password is strong else False.

    Strong password requirements include:  
    - At least 8 characters
    - Contains both uppercase and lowercase characters
    - At least one digit
    """
    strong_regex = re.compile(r'''
        ^(?=.*?[a-z])  # Contains at least one lowercase letter
        (?=.*?[A-Z])   # Contains at least one uppercase letter
        (?=.*?[0-9])   # Contains at least one digit
        .{8,}$         # At least 8 characters
        ''', re.VERBOSE)

    return bool(strong_regex.search(password))


if __name__ == '__main__':
    password = input('Enter your password: ')
    if strong_password(password):
        print('Your password is strong!')
    else:
        print ('Your password is weak. It should be at least eight characters, contain uppercase and lowercase characters, and contain at least one digit.')