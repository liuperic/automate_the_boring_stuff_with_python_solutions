#!/usr/bin/env/python3
# Regex to detect dates in DD/MM/YYYY format

# Per specs: regular rexpression does not have to detect correct days for each
# month or leap year; it will accept nonexistent dates like 31/02/2020.
# Store strings into month, day, and year

import re, sys

date_regex = re.compile(r'''^(0[1-9]|[1-2][0-9]|3[0-1])/     # Date DD/ format
                    (0[1-9]|1[0-2])/   # MM/ months
                    ([1-2][0-9]{3})   # YYYY years      
                    ''', re.VERBOSE)

def valid_date(day, month, year):
    # Check for leap year
    leap_year = False
    if year % 4 == 0 and not year % 100 == 0:   # Is leap year if divisible by 4 and not divisible by 100
        leap_year = True
    elif year % 4 == 0 and (year % 100 == 0 and year % 400 == 0):    # Is leap year if divisible by 4 and 100, if also divisible by 400
        leap_year = True
    
    if month in ['04', '06', '09', '11']:    # Checks if month is Apr, June, Sept, or Nov (30 day months)
        if day > 30 or day < 1: return False
    elif month == 2 and not leap_year:   # 28 days in non-leap year February
        if day > 28 or day < 1: return False
    elif month == 2 and leap_year:
        if day > 29 or day < 1: return False      # 2 days in leap year February
    else:
        if day > 31 or day < 1: return False
    
    return True   # True / valid date if passes all tests

if __name__ == '__main__':
    try:
        date = input('Enter a date in DD/MM/YYYY format: ')

        # Convert string groups into ints
        day = int(date_regex.search(date).group(1))
        month = int(date_regex.search(date).group(2))
        year = int(date_regex.search(date).group(3))
    except AttributeError: 
        print('Invalid date format. Please try again! DD/MM/YYYY')
        print('Valid days include 01 to 31; valid months include 01 to 12; valid years include 1000 to 2999')
        sys.exit(1)

    if valid_date(day, month, year):
        print('%s is a valid date!' % date_regex.search(date).group(0))
    else:
        print('%s is not a valid date. Please try again' % date_regex.search(date).group(0))