array = [k+1 for k in range(30)]
arr = [int(input()) for i in range(28)]

for j in range(28):
    array.remove(arr[j])

max = max(array)
min = min(array)

print(min)
print(max)