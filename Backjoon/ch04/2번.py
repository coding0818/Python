n, x = map(int, input().split())
arr = list(map(int, input().split()))

for k in range(n):
    if arr[k] < x:
        print(arr[k], end=' ')
    else:
        pass