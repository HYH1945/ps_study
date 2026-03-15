import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
# bit masking, DP

# n = 4일때
# visited = 0000 (2진수)
# dp[n][n * n]으로 구성
# dp[curr][visited] : 현재 위치가 curr이고 visited 방문한 상태에서 최소비용
# dp[3][0111] 현재위치가 3, 1,2,3번 도시 방문함

matrix = []
visited = 0b0000
INF = 1e9
dp = [[INF] * (2**n) for _ in range(n)]

for _ in range(n):
    matrix.append(list(map(int, input().split())))

queue = deque()
visited = 0b0001 # 0(1)번도시부터 시작
dp[0][visited] = 0
queue.append((0, visited))

answer = [INF] * n

#def tsp():

while queue:
    curr, visited = queue.popleft()
    
    #방문 끝
    if visited == (1 << n) - 1: 
        continue
    #방문중
    else:
        for i in range(1, n): #초기상태 : 0번도시라 1번도시부터 n번까지 방문
            #print(matrix[curr][i], visited & (1 << i))
            if matrix[curr][i] != 0 and (visited & (1 << i) == 0): # 갈수있고, 방문한적이 없는도시
                if dp[curr][visited] + matrix[curr][i] < dp[i][visited | 1 << i]:
                    dp[i][visited | 1 << i] = dp[curr][visited] + matrix[curr][i]
                    queue.append((i, visited | (1 << i)))
answer = INF
for i in range(1, n):
    if matrix[i][0] != 0:
        answer = min(answer, dp[i][(1<<n)- 1] + matrix[i][0])
print(answer)
