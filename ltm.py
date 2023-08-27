# For long term memory

import os
import random
import datetime
import time

os.system('cls')

total_digits = 6
time_limit = 5
extra_time = 0.5
attempts = 0
score = 0
best_level = 6
try:
    while (True):
        os.system('cls')
        nums = []
        for i in range(total_digits):
            num = random.choice(range(10))
            print(num, end='')
            nums.append(num)
        print()
        time.sleep(time_limit)
        os.system('cls')    
        answer = input('Answer (or enter -1 to quit): ')
        if (answer == '-1'):
            break
        correct = True
        for num, ans in zip(nums, answer):
            if (num != int(ans) or len(nums) != len(answer)):
                print('Wrong Answer!')
                total_digits -= 1
                time_limit -= extra_time
                print('Correct Answer:', end=' ')
                for num in nums:
                    print(num, end='')
                print()
                input('Press Enter to continue')
                correct = False
                break
        if (correct):
            print('Correct Answer!')
            total_digits += 1
            time_limit += extra_time
            if total_digits > best_level:
                best_level = total_digits
            score += 1
            input('Press Enter to continue')
        attempts += 1
finally:
    print('Total:', attempts)
    print('Score:', score)
    print('Max level reached:', best_level)
    try: 
        print('Accuracy:', round((score/attempts) * 100, 2))
    finally:
        print('Terminating Program')
        time.sleep(2)
    
            


