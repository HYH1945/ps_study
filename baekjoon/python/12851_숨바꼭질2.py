import sys
from collections import deque

# 기존 숨바꼭질코드 : curr == k이면 바로 break
# 차이점 : break 안걸고 continue, dist 배열 최대크기 전부 방문하며 테스트
# 그리고 next 노드 방문할때 방문안한점외에도 바로 다음점의 비용을 체크,
# bfs 특성상 이미 한번 방문된 경로의 비용은 항상 최단경로지만
# 약간 다른방법으로 중복된 최단경로가 존재할 수 있음
# 그래서 이미 방문한점을 방문하게될때도 dist[next] == dist[curr] + 1:, 즉 최단경로로 방문할 수 있다면 그 경우의수를 체크해봄(원래 무시했지만)

input = sys.stdin.readline

n, k = map(int, input().split())

dist = [-1] * 100001
dist[n] = 0

minimum_time = float('inf')
count = 0
queue = deque()
queue.append(n)
while queue:
    curr = queue.popleft()

    if dist[curr] > minimum_time:
        continue

    # 찾음
    if curr == k:
        # 최적이면
        if dist[curr] < minimum_time:
            minimum_time = dist[curr]
            count = 1
        
        # 최적인거 한번더찾음
        elif dist[curr] == minimum_time:
            count += 1
        continue

    for next in (curr-1, curr+1, 2*curr):
        if 0<= next < 100001:
            if dist[next] == -1 or dist[next] == dist[curr] + 1: # 방문 X 또는 이미 방문했어도 최적의 비용으로 방문하는경우
                dist[next] = dist[curr] + 1
                queue.append(next)

print(dist[k])
print(count) 