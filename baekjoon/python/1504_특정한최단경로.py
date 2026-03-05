import sys
import heapq
input = sys.stdin.readline

n, e = map(int, input().split())
adj_list = [[] for _ in range(n+1)]

for _ in range(e):
    a, b, c= map(int, input().split())
    adj_list[a].append((b,c))
    adj_list[b].append((a,c))

x, y = map(int, input().split())

distance = [float('inf')] * (n + 1)

def dijkstra(start):
   
    distance[start] = 0

    pq = [(0, start)] # (누적거리, 번호)

    while pq:
        curr_dist, curr_node = heapq.heappop(pq)

        if distance[curr_node] < curr_dist:
            continue

        for neighbor, weight in adj_list[curr_node]:
            new_dist = curr_dist + weight

            if new_dist < distance[neighbor]:
                distance[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))


# 최단거리 케이스
# 1 -> v1(x) -> v2(y) -> n
# 1 -> v2(y) -> v1(x) -> n

dijkstra(1)

v1_dist = distance[x]
v2_dist = distance[y]

distance = [float('inf')] * (n + 1)
dijkstra(x)

v1_n_dist = distance[n]
v1_v2_dist = distance[y]

distance = [float('inf')] * (n + 1)
dijkstra(y)
v2_n_dist = distance[n]

answer = min(v1_dist + v1_v2_dist + v2_n_dist, v2_dist + v1_v2_dist + v1_n_dist)

if answer == float('inf'):
    print(-1)
else:
    print(answer)