a= int(input())
b= int(input())
c= int(input())
d= int(input())
e= int(input())
f= int(input())
g= int(input())
h= int(input())
i= int(input())

arr = [a, b, c, d, e, f, g, h, i]

max = arr[0]
maxcount = 0

for i in range(1,9):
    if max < arr[i]:
        max = arr[i]
        maxcount = i+1

print(max)
print(maxcount)



