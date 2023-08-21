import random
import os
import time

nums = range(10)
print('Choose difficulty:')
print('1: Easy')
print('2: Still Easy')
print('3: Medium')
print('4: Kinda Hard')
print('5: Hard')
print('6: Very Hard')
print('7: Impossible')

diff = int(input()) + 3
rows = int(diff / 2)
cols = diff - rows
os.system('cls')
score = [0, 0]
try:
    while True:
        matrix = []
        for i in range (rows):
            matrix.append([])
        for i in range(rows):
            for j in range(cols):
                matrix[i].append(random.choice(nums))
                print(matrix[i][j], end=' ')
            print()
        time.sleep(1)
        os.system('cls')
        x = random.choice(range(rows))
        y = random.choice(range(cols))
        for i in range(rows):
            for j in range(cols):
                if (i == x and j == y):
                    print('_', end='')
                else:
                    print('#', end='')
            print()
        print('Enter -1 to quit')
        ans = int(input('Fill the blank: '))
        if ans == -1:
            break
        if ans == matrix[x][y]:
            print('Correct!')
            score[0] += 1
        else:
            print('Wrong!')
        score[1] += 1
        time.sleep(0.5)
        os.system('cls')
finally:
    if (score[1] != 0):
        print('Total:', score[1])
        print('Accuracy:', round(score[0] * 100 / score[1]), end='')
        print('%')
    print('Thanks for Playing!')
    time.sleep(3)
    
    
    
    