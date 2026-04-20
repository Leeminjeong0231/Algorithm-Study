import sys
n, k = map(int, sys.stdin.readline().split())

coins = list(map(int, sys.stdin.read().split()))

coins.sort(reverse=True)
num = 0

for i in coins:
    if k == 0:
        break
    num += k//i
    k %=i

print(num)