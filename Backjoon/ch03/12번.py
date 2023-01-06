n = int(input())
b = (n % 10 + n // 10)%10 + n % 10 * 10
i = 1
while b != n:
    i += 1
    b = (b % 10 + b // 10)%10 + b % 10 * 10

print(i)    