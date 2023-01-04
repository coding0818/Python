import sys

t = int(sys.stdin.readline())

for num in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)