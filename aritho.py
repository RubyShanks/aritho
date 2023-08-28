import random
import os
import time
import datetime

os.system('cls')
session_start = datetime.datetime.now()
print('Choose difficulty:')
print('1: Vanilla')
print('2: Amateur 1')
print('3: Amateur 2')
print('4: Challenger')
print('5: Expert')
print('6: Pro')
print('7: World Class')
print('8: World Champion')
print('9: Insane')
print('10: Legendary')
print('15: God Mode')
diff = int(input())
num_limit = 10 ** diff
is_timed = input('Do you want to pre-set a session time limit? (y/n): ')
session_time_limit = 600
if (is_timed == 'y'):
    is_timed = True
    session_time_limit = int(input('Enter session time limit (in minutes): '))

score = 0
resptimes = []
total_attempts = 0
os.system('cls')
totresptime = 0
try: # If an error occurs program should show results before quitting. 
    while True:
        num1 = random.choice(range(num_limit))
        num2 = random.choice(range(num_limit))
        print('Enter -1 to quit')
        print(num1, '+', num2, '= ', end='')
        before_response = datetime.datetime.now()
        answer = int(input())
        after_response = datetime.datetime.now()
        response_time = after_response - before_response
        if answer == -1:
            break
        if (is_timed and (totresptime + response_time.total_seconds()) / 60 >= session_time_limit):
            print('Time Up!')
            break
        resptimes.append(response_time.total_seconds())
        totresptime += response_time.total_seconds()
        if answer == (num1 + num2):
            print ('Correct!')
            score += 1
        else:
            print('Wrong!')
            print('Answer:', num1 + num2)
        print('Response Time:', round(response_time.total_seconds(), 2), end='')
        print('s')
        total_attempts += 1
        input('Press Enter to continue')
        os.system('cls')
finally:
    resptimes.sort() # Sorted to find median of data
    print('Total                : ', total_attempts)
    print('Score                : ', score)
    try:
        print('Accuracy             :', round(score * 100 / total_attempts, 1), end='')
        print('%')
        print('Median response time :', round(resptimes[int(len(resptimes) / 2)], 1), end='')
        print('s')
        print('Average response time:', round(totresptime / total_attempts, 1), end='')
        print('s')
    finally:
        print('Terminating Program.')
        print('Thanks for Playing!')
        session_end = datetime.datetime.now()
        session_duration = session_end - session_start
        print('Session Time:', int(session_duration.total_seconds() / 60), 'minutes')
        time.sleep(3)
        