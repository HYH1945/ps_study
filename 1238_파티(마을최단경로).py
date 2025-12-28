import sys
import heapq

input = sys.stdin.readline

n, m, x = map(int, input().split())

adj_list = [[] for _ in range(m+1)]
for i in range(m):
    u, v, w = map(int, input().split())
    adj_list[u].append((v, w))

def dijkstra(start, goal):
    pq = []
    distance = [float('inf')] * (m+1)
    heapq.heappush(pq, (0, start))
    distance[start] = 0

    while pq:
        dist, now = heapq.heappop(pq)

        if distance[now] < dist:
            continue

        for i in adj_list[now]:
            cost = dist + i[1] # i[1] : weight
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(pq, (cost, i[0])) # i[0] : 도착지
    return distance[goal]

answer = []

for i in range(1, n+1):
    answer.append(dijkstra(i, x) + dijkstra(x, i))

print(max(answer))