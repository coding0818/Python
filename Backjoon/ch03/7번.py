x = int(input())

for n in range(x):
    a, b = map(int, input().split())
    print('Case #{}: {} + {} = {}'.format(n+1,a,b,a+b))