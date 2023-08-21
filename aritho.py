import random
import os
import time
import datetime

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
diff = int(input())
num_limit = 10 ** diff
score = 0
resptimes = []
total_attempts = 0
os.system('cls')
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
        resptimes.append(response_time.total_seconds())
        if answer == (num1 + num2):
            print ('Correct!')
            score += 1
        else:
            print('Wrong!')
        print('Response Time:', round(response_time.total_seconds(), 2), end='')
        print('s')
        total_attempts += 1
        time.sleep(1.5)
        os.system('cls')
finally:
    totresptime = 0
    for resptime in resptimes:
        totresptime += resptime
    resptimes.sort() # Sorted to find median of data
    print('Total                : ', total_attempts)
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
        