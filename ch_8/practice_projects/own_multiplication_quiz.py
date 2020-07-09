#!usr/bin/env python3

# Recreate multiplication quiz from chapter projects
# without using pyinputplus

from threading import Timer
import random, time

number_of_questions = 10
correct_answers = 0
start_time = 0

for question_number in range(1, number_of_questions + 1):
    # Pick two random numbers:
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)

    prompt = '#%s: %s x %s = ' % (question_number, num1, num2)

    
    tries = 0
    while True:
        if(start_time == 0):
            start_time = time.time()
        try:
            answer = int(input(prompt))
        except ValueError:
            print('Not a number, please try again')
            continue
        tries += 1
        if answer == num1 * num2:
            print('Correct!')
            correct_answers += 1
            break
        elif((time.time()-start_time)>=8):
            print('Out of time.')
            break
        elif tries == 3:
            print('Out of tries!')
            break
        print('Incorrect')

    time.sleep(1) # Brief pause to let user see the result.
print('Score: %s / %s' % (correct_answers, number_of_questions))
