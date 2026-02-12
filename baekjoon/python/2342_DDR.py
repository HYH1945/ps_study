import sys

input = sys.stdin.readline

arr = list(map(int, input().split()))

n = len(arr) - 1

dp = [[[float('inf')] * 5 for _ in range(5)] for _ in range(n + 1)]

# dp[step][left][right] : step 단계에서 왼발 오른발을 (left, right)에 뒀을때 드는 힘 총합

# start -> end 가는 비용 반환
def move(start, end):
    if start == 0:
        return 2
    elif abs(start-end) == 1 or abs(start-end) == 3: # 인접한 위치 이동
        return 3
    elif abs(start-end) == 2: # 건너편 이동
        return 4
    if start == end: # 같은 경우
        return 1

dp[0][0][0] = 0

for i in range(1, n+1):
    target = arr[i-1] 

    for left in range(5):
        for right in range(5):
            # dp[i][left][right] : 현재위치
            # target : 이동할 위치

            if dp[i-1][left][right] == float('inf'): # 이전 step이 불가능
                continue
            
            if target != right: # 왼발을 target으로 옮김 (target == right인 경우 오른발 옮기면됨)
                
                dp[i][target][right] = min(dp[i][target][right], dp[i-1][left][right] + move(left, target))

                # min 함수 설명
                # dp[i][target][right] : 이미 다른 경로를 통해 현재 단계(i)에서 똑같은 발 모양(left, target)을 만든 적이 있는지 확인
                # dp[i-1][left][right] + move(left, target) : 이전 단계에서 왼발을 target으로 옮긴경우

                # 즉 이미 계산된 경로와 지금 계산하는 경로 비용 비교

            if target != left : # 오른발을 target으로 옮김
                dp[i][left][target] = min(dp[i][left][target], dp[i-1][left][right] + move(right, target))

answer = float('inf')

for left in range(5):
    for right in range(5):
        answer = min(answer, dp[n][left][right]) # 마지막 단계(모든 step을 진행완료) 경우의수중 최솟값

print(answer)