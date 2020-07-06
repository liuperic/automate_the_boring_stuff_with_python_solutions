#!/usr/bin/env python3

def comma_code(list):
    combined_list = ''
    for item in list:   
        if item != list[len(list) - 1]:
            combined_list += str(item) + ', '   # use str to convert all non-string elements to string type
        else:
            combined_list += 'and ' + str(item)     # use str to convert all non-string elements to string type

    return combined_list
