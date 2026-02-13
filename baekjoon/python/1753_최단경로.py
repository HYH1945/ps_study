# 1753 최단경로 : 벨만포드, 다익스트라, Acylic
import sys
import heapq

input = sys.stdin.readline

v, e = map(int, input().split())

k = int(input())


adj_list = [[] for _ in range(v+1)]
distance = [float('inf')] * (v+1)


for i in range(e):
    u, b, w = map(int, input().split())
    adj_list[u].append(((b, w)))

pq = []

heapq.heappush(pq, (0, k))
distance[k] = 0

while pq:
    dist, now = heapq.heappop(pq)

    if distance[now] < dist:
        continue

    for i in adj_list[now]:
        cost = dist + i[1] # i[1] : weight
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(pq, (cost, i[0])) # i[0] : 도착지

for i in range(1, v + 1):
    if(distance[i] == float('inf')):
        print("INF")
    else:
        print(distance[i])

