import sys
n = int(sys.stdin.readline())

tringle = []
for _ in range(n):
    tringle.append(list(map(int, sys.stdin.readline().split())))

dp = [[0] * n for _ in range(n)]
dp[0][0] = tringle[0][0]


for i in range(1, n):
    for j in range(1 + i):
        if j == 0:
            dp[i][j] = dp[i-1][j] + tringle[i][j]
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + tringle[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + tringle[i][j]

print(max(dp[n-1]))