#!/usr/bin/env python3

# Collatz sequence with exception handling for invalid integers.
def collatz():
    print('Please enter an integer greater than 1 for collatz sequence')
    try:
        number = int(input())
        while number != 1:
            if number % 2 == 0:
                print(number // 2)
                number = number // 2
            else:
                print(number * 3 + 1)
                number = number * 3 + 1
    except ValueError:
        print('Please enter a valid integer.')

collatz()
