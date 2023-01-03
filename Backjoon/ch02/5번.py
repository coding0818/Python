a, b = map(int, input().split())

if b < 45:
    b = b + 15
    if a == 0:
        a = a + 23
    else:
        a = a - 1
elif b >= 45:
    b = b - 45


print(a, b)

    
    