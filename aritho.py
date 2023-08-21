import random
import os
import time
import datetime

session_start = datetime.datetime.now()
nums = range(int(1e4))
score = [0, 0]
totresptime = 0
resptimes = []
try:
    while True:
        x = random.choice(nums)
        y = random.choice(nums)
        print('Enter -1 to quit')
        print(x, '+', y, '= ', end='')
        before = datetime.datetime.now()
        ans = int(input())
        after = datetime.datetime.now()
        interval = after - before
        totresptime += interval.total_seconds()
        resptimes.append(interval.total_seconds())
        if ans == -1:
            break
        if ans == (x + y):
            print ('Correct!')
            score[0] += 1
        else:
            print('Wrong!')
        print('Response Time:', round(interval.total_seconds(), 2), end='')
        print('s')
        score[1] += 1
        time.sleep(1.5)
        os.system('cls')
finally:
    resptimes.sort()
    print('Total                : ', score[1])
    try:
        print('Accuracy             :', round(score[0] * 100 / score[1], 1), end='')
        print('%')
        print('Median response time :', round(resptimes[int(len(resptimes) / 2)], 1), end='')
        print('s')
        print('Average response time:', round(totresptime / score[1], 1), end='')
        print('s')
    finally:
        print('Thanks for Playing!')
        session_end = datetime.datetime.now()
        interval = session_end - session_start
        print('Session Time:', int(interval.total_seconds() / 60), 'minutes')
        time.sleep(3)
        