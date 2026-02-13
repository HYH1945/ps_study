import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = []
answer = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

dp = [[0] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):

        #dp[i][j] : (i,j)까지의 합
        #arr[i-1][j-1]인 이유 : dp배열은 dp[0][~]와 dp[~][0]은 일부러 패딩해뒀기에 1차이가 남
        dp[i][j] = arr[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] #(i-1, j)까지의 합은 세로직사각형, (i, j-1)까지의 합은 가로직사각형, 둘이 더하면 (i-1, j-1)까지의 합이 두번 더해지므로 뺌.

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())

    # 구간합 로직 구하는거와 마찬가지
    answer.append(dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1])

for item in answer:
    print(item)