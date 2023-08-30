import random
import os
import time
import datetime

os.system('cls')

session_start = datetime.datetime.now()

nums = range(10) # Matrix elements 0-
flashtime = 1

print('Choose difficulty:')
print('1: Easy')
print('2: Still Easy')
print('3: Medium')
print('4: Kinda Hard')
print('5: Hard')
print('6: Very Hard')
print('7: Impossible')

difficulty = int(input()) + 3
rows = int(difficulty / 2)
cols = difficulty - rows
os.system('cls')
score = 0
totalattempts = 0
try:
    while True:
        matrix = []
        for i in range(rows):
            matrix.append([])
            for j in range(cols):
                matrix[i].append(random.choice(nums))
                print(matrix[i][j], end=' ')
            print()
        time.sleep(flashtime)
        os.system('cls')
        num1 = random.choice(range(rows))
        num2 = random.choice(range(cols))
        for i in range(rows):
            for j in range(cols):
                if (i == num1 and j == num2):
                    print('_', end='')
                else:
                    print('#', end='')
            print()
        print('Enter -1 to quit')
        ans = int(input('Fill the blank: '))
        if ans == -1:
            break
        if ans == matrix[num1][num2]:
            print('Correct!')
            score += 1
        else:
            print('Wrong!')
        totalattempts += 1
        time.sleep(0.5)
        os.system('cls')
finally:
    if (totalattempts != 0):
        print('Total:', totalattempts)
        print('Accuracy:', round(score * 100 / totalattempts, 2), end='')
        print('%')
    print('Thanks for Playing!')
    session_end = datetime.datetime.now()
    session_duration = session_end - session_start
    print('Session duration: ', round(session_duration.total_seconds() / 60), 'minutes')
    time.sleep(3)
    
    
    
    