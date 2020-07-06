#!/usr/bin/env python3

import random

# Estimates probability of six heads or tails occurring in 100 random coin flips.
# Repeats experiment of 100 coin flips 10,000 times.
number_of_streaks = 0
for experiment_num in range(10000): # Run experiment 10000 times
    current_streak = 1  # Initiate streak as 1 since all individual flips are streaks of 1
    flips = []
    new_streak = False
    for i in range(100):
        current_flip = random.randint(0, 1)   

        if current_flip == 0:
            flips.append('H')
        else:
            flips.append('T')

        if i == 0:
            continue                # Nothing to compare at first iteration
        elif new_streak == True:    # Ensures once new streak starts, last flip is not being compared
            new_streak = False      # since we want a clean reset streak, similar to when i == 0 
            continue
        else:
            last_flip = flips[i-1] 
            if last_flip == flips[i]:
                current_streak += 1
                if current_streak == 6:     # Once streak is 6, reset streak to 1 and increment streak counter
                    number_of_streaks += 1
                    current_streak = 1
                    new_streak = True   # New streak found, flip boolean so last flip will not be compared on follow iteration.
            else:
                current_streak = 1  # Reset streak since streak is over

print('Chance of streak: %s%%' % (number_of_streaks / 10000))   # total number of streaks divided by total number of experiments to get probability.

# Sample probability results are roughly ~1.50%, similar to theoretical probability of (50%)^6 = 1.56%.