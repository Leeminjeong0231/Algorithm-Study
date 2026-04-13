import sys

t = int(sys.stdin.readline())

#f(n) = f(n-1) + f(n-2) +f(n-3), f>3

p = [0] * 11
p[1] = 1
p[2] = 2
p[3] = 4

for i in range(4, 11):
    p[i] = p[i-1] + p[i-2] + p[i-3]

for _ in range(t):
    n = int(sys.stdin.readline())
    print(p[n])