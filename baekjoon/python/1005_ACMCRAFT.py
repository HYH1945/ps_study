import sys
from collections import deque

input = sys.stdin.readline

# directed graph
# topological sort + DP
# 복습 필요

T = int(input())
answer = []

for _ in range(T):
    
    N, K = map(int, input().split())
    cost = [0] + list(map(int, input().split())) # 인덱스 padding
    in_degree = [0] * (N+1)

    # dp[i] = i번째 건물을 지을 수 있는 최소시간
    dp = [0] * (N+1)
    queue = deque()
    adj_list = [[] for _ in range(N+1)]
    for _ in range(K):
        u, v = map(int,input().split())
        adj_list[u].append(v)
        in_degree[v] += 1
    W = int(input())
    
    # 진입 차수 0: 그냥 그 건물 짓는 코스트가 최소 cost (맨첨에 지어야함)
    for i in range(1, N+1):
        if in_degree[i] == 0:
            queue.append(i)
            dp[i] = cost[i]
    
    while queue:
        curr = queue.popleft()

        for next in adj_list[curr]:
            dp[next] = max(dp[next], dp[curr] + cost[next])
            in_degree[next] -= 1

            if in_degree[next] == 0:
                queue.append(next)
    
    answer.append(dp[W])

for item in answer:
    print(item)