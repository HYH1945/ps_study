import sys
input = sys.stdin.readline

# DP, 삼각형 문제와 비슷

n = int(input())

home = [[0] * n for _ in range(n)]

dp = [[0] * 3 for _ in range(n)]

for i in range(n):
    home[i][0], home[i][1], home[i][2] = map(int,input().split())

for i in range(n):
    for j in range(3):
        if i == 0:
            dp[i][j] = home[i][j] 
        else:
            if j == 0: # 빨
                dp[i][j] += home[i][j] + min(dp[i-1][j+1], dp[i-1][j+2])
            elif j == 2: # 파
                dp[i][j] += home[i][j] + min(dp[i-1][j-2], dp[i-1][j-1])
            else: #초
                dp[i][j] += home[i][j] + min(dp[i-1][j-1], dp[i-1][j+1])

print(min(dp[n-1]))
