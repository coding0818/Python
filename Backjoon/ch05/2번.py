def solve(n):
    a = n//10000
    b = (n//1000)%10
    c = (n//100)%10
    d = (n//10)%10
    e = n%10

    return n+a+b+c+d+e

all = [i+1 for i in range(10000)]
selfnumber = []
for k in all:
    c = solve(k)
    if c<=10000:
        selfnumber.append(c)

for j in selfnumber:
    all.remove(j)

for ans in all:
    print(ans)