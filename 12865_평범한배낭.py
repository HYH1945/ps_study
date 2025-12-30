import sys
# DP 문제였음,, (memoization)

# 물건을 배열에 다 저장하고
# dp[i][j] << 현재 무게한도가 j라고 했을 때 i번째 물건까지 고려한 배낭의 최대 가치 
# j를 1부터 k까지 점차 증가시키며 계산

input = sys.stdin.readline

n, k = map(int, input().split())

item = [[0,0]] # 인덱스 1부터 고려하도록

dp = [[0 for col in range(k+1)] for row in range(n+1)]

for i in range(n):
    w, v = map(int, input().split())
    item.append([w,v])

for i in range(1, n+1):
    weight, value = item[i]
    for j in range(1, k+1):
        if j < weight: # 현재 물건 무게가 한도보다 큼
            dp[i][j] = dp[i-1][j] # 이전에 고려한 최적해 (해당 물건을 안넣었을때)
        else: # 넣을 수 있음
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value) #dp[i-1][j-weight] : 남은 무게에서 가장 최적의 가치, value : 현재 넣는 물건 가치

print(dp[n][k])

