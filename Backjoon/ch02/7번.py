a, b, c = map(int, input().split())
price = 0

if a == b == c:
    price = 10000+a*1000
elif a == b != c or a == c != b:
    price = 1000 + a * 100
elif b == c != a:
    price = 1000 + b * 100
else:
    if a > b and a > c:
        price = a * 100
    elif b > a and b > c:
        price = b * 100
    elif c > a and c > b:
        price = c * 100

print(price)