import sys
from collections import deque
input = sys.stdin.readline

n, d = map(int, input().split())


dist = [float('inf')] * (d+1)
shortcut = [[] for _ in range(d+1)]

for _ in range(n):
    start, end, cost = map(int, input().split())
    
    if end <= d:
        shortcut[start].append((end, cost))

dist[0] = 0

for i in range(d+1):
    if i > 0:
        dist[i] = min(dist[i], dist[i-1] + 1)
    
    for next_pos, cost in shortcut[i]:
        if dist[next_pos] > dist[i] + cost:
            dist[next_pos] = dist[i] + cost

print(dist[d])

# print(dist)
