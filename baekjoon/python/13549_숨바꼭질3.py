import sys
from collections import deque

# bfs
input= sys.stdin.readline

n, k = map(int, input().split())

MAX = 100001

dist = [-1] * MAX

q = deque([n])

dist[n] = 0 #시작점 dist[n]

while q:
    now = q.popleft()

    if now == k:
        print(dist[now])
        break
    
    #순간이동
    if 0 <= now * 2 < MAX and dist[now*2] == -1: # 순간이동한 곳을 방문한 적이 없고 범위 안이라면
        dist[now*2] = dist[now] # 비용 0 (0초)
        q.appendleft(now * 2) # 0초 걸리는 행동을 우선시해야
    print(q)
    #걷기
    for next in (now - 1 , now + 1):
        if 0 <= next < MAX and dist[next] == -1: #걸어갈 곳을 방문한 적이 없고 범위 안이라면
            dist[next] = dist[now] + 1
            q.append(next)
