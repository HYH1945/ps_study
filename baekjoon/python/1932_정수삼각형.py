import sys
input = sys.stdin.readline

# DP

n = int(input())

triangle = []
dp = [[0] * (n) for _ in range(n+1)]

for _ in range(n):
    triangle.append(list(map(int,input().split())))

for i in range(1,n+1):
    for j in range(i):
        if j == 0:
            dp[i][j] += triangle[i-1][j] + dp[i-1][j]
        elif j == i:
            dp[i][j] += triangle[i-1][j] + dp[i-1][j-1]
        else:
            dp[i][j] += triangle[i-1][j] + max(dp[i-1][j-1], dp[i-1][j])
        
print(max(dp[n]))