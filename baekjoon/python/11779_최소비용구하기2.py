import sys
import heapq

input = sys.stdin.readline

n = int(input())
m = int(input())

adj_list = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    adj_list[u].append((v, w))
start, end = map(int, input().split())

def dijkstra(start):
    distance = [float('inf')] * (n+1)
    pq = []
    heapq.heappush(pq, (0, start))
    distance[start] = 0
    parent = [-1] * (n+1)
    parent[start] = start

    # for vertex, weight in adj_list[start]:
    #     heapq.heappush(pq, (vertex, weight))
    
    while pq:
        dist, now = heapq.heappop(pq)

        #print(f'dist: {dist} now: {now}')
        if distance[now] < dist:
            continue
        
        for i in adj_list[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                parent[i[0]] = now
                #print(parent)
                heapq.heappush(pq, (cost, i[0]))
    return distance, parent

distance, parent = dijkstra(start)

answer = []

print(distance[end])
while True:
    answer.append(end)
    if parent[end] == end:
        break
    end = parent[end]
print(len(answer))
for i in range(len(answer)-1, -1, -1):
    print(answer[i], end=" ")