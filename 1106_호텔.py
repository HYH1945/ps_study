import sys

# unbounded knapsack

# dp[i] = i명을 모으는데 드는 최소 비용

input = sys.stdin.readline

c, n = map(int, input().split())

dp = [float('inf')] * (c + 101) # 100 :  그 비용으로 얻을 수 있는 고객의 수가 주어진다. 이 값은 100보다 작거나 같은 자연수이다.

# 최소 10명 모으는 최소비용이 필요하면
# 복잡하게 생각할 거 없이
# 11명, 12명, 13명 ~ 모으는 최소비용을 각각 다 구해서
# 그중에서 최소값을 때리기

arr = []

for _ in range(n):
    cost, customer = map(int, input().split())
    arr.append((cost, customer))

dp[0] = 0
for cos, cus in arr:
    for i in range(cus, c+101):
        # 그대로 (dp[i]) or dp[i-cus] : 만약 현재 i 가 5고 cus가 3이라면, dp[2]는 2명모을때 최소비용이 저장되어있으므로 그거 더하기 3을 때린것과 dp[i]를 비교한 최소값을 구하면 최소비용
        dp[i] = min(dp[i], dp[i-cus] + cos) # 변수명 주의


print(min(dp[c:]))