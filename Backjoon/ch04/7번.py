n = int(input())
a = list(map(int, input().split()))

max = max(a)
total = 0
for k in a:
    total += k

average = (total / n) / max * 100
print(average)