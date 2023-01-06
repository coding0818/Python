n = int(input())
arr = list(map(int, input().split()))
max = arr[0]
min = arr[0]

for i in arr[1:]:
    if min > i:
        min = i
    elif max < i:
        max = i
        

print(min, end=' ')
print(max)