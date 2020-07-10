#!/usr/bin/env python3
# mcb.pyw - Saves and loads pieces of text to the clipboard
# Usage: py.exe mcb2.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb2.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb2.pyw list - Loads all keywords to clipboard.
#        py.exe mcb2.pyw delete <keyword> - Deletes a keyword from the shelf
#        py.exe mcb2.pyw delete_all - Deletes all keywords
import shelve, pyperclip, sys

mcb_shelf = shelve.open('mcb')

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcb_shelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del mcb_shelf[sys.argv[2]]
    print(sys.argv[2] + ' has been deleted')
    pyperclip.copy('')

elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])
    elif sys.argv[1].lower() == 'delete_all':
        for key in mcb_shelf:
            del mcb_shelf[key]
            print('All keywords have been deleted')
        pyperclip.copy('')

mcb_shelf.close()