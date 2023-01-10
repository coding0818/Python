arr = [int(input()) for k in range(9)]

max = arr[0]
maxcount = 1

for i in range(1,9):
    if max < arr[i]:
        max = arr[i]
        maxcount = i+1

print(max)
print(maxcount)



