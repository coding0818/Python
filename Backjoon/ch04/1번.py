n = int(input())
a = list(map(int, input().split()))

v = int(input())

count = 0
for k in range(n):
    if a[k] == v:
        count += 1
    else:
        pass

print(count)