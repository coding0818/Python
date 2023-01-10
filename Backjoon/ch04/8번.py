n = int(input())
arr = [input() for k in range(n)]

for k in arr:
    count = 0
    score = 0
    str = list(k)
    for s in str:
        if s == 'O':
            count += 1
            score += count
        else:
            count == 0
    print(score)
