import math

c = int(input())
for k in range(c):
    score = list(map(int, input().split()))
    total = 0
    for n in range(1,len(score)):
        total += score[n]
    aver = total / score[0]
    count = 0
    for j in range(1, len(score)):
        if aver < score[j]:
            count += 1
    per = format(round(count / score[0] * 100, 3), '.3f')

    print('{}%'.format(per))
