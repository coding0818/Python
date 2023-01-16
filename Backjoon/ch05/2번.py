def solve(n):
    a = n//10000
    b = (n//1000)%10
    c = (n//100)%10
    d = (n//10)%10
    e = n%10

    return n+a+b+c+d+e

all = [i for i in range(1,10001)]
selfnumber = []
for k in all:
    c = solve(k)
    if c<=10000:
        selfnumber.append(c)

selfnumber = set(selfnumber)
selfnumber = list(selfnumber)

ans = [a for a in all if a not in selfnumber]

for s in ans:
    print(s)