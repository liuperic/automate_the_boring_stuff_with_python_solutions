#!/usr/bin/env python3

def collatz():
    print('Please enter an integer greater than 1 for collatz sequence')
    number = int(input())
    while number != 1:
        if number % 2 == 0:
            print(number // 2)
            number = number // 2
        else:
            print(number * 3 + 1)
            number = number * 3 + 1

collatz()
