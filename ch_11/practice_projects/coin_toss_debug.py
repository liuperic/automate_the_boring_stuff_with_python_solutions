#!/usr/bin/env python3

"""
Find the bugs in the program and fix

Original code:

import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0,1) # 0 is tails, 1 is heads
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope, you are really bad at this game.')
"""

import random

guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    if guess == 'heads':    # Need to convert guess string into int for heads or tails
        guess_convert = 1   # 1 = heads
    elif guess == 'tails':
        guess_convert = 0   # 0 = tails
toss = random.randint(0,1) # 0 is tails, 1 is heads
if toss == guess_convert:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if guess == 'heads':
        guess_convert = 1   # 1 = heads
    elif guess == 'tails':
        guess_convert = 0   # 0 = tails
    if toss == guess_convert:
        print('You got it!')
    else:
        print('Nope, you are really bad at this game.')