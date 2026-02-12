import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

dist = [-1] * (100001)
dist[N] = 0

time = 0
queue = deque()

# 시작
queue.append(N)

while queue:
    curr = queue.popleft()

    if curr == K:
        break

    # 걷기, 순간이동이 모두 1초
    # -> 첨 방문하면 무조건 최소시간
    for next in (curr-1, curr+1, 2*curr):
        if 0 <= next < 100001 and dist[next] == -1:
            dist[next] = dist[curr] + 1
            queue.append(next)

print(dist[K])