import sys
import heapq

input = sys.stdin.readline

n = int(input())
m = int(input())

adj_list = [[] for _ in range(n+1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    adj_list[u].append((v,w))

src, dst = map(int, input().split())

def dijkstra(start, goal):
    pq = []
    dist = [float('inf')] * (n+1)

    heapq.heappush(pq, (0, start))
    dist[start] = 0
    
    while pq:
        distance, now = heapq.heappop(pq)
        if dist[now] < distance:
            continue

        for v, w in adj_list[now]:
            if distance + w < dist[v]:
                dist[v] = distance + w
                heapq.heappush(pq, (dist[v], v))
    return dist[goal]

print(dijkstra(src, dst))