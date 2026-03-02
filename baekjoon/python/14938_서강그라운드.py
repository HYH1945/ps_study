import sys
import heapq
input = sys.stdin.readline

n, m, r = map(int, input().split())
item = list(map(int, input().split()))

adj_list = [[] for _ in range(n+1)]

for _ in range(r):
    a,b,l = map(int, input().split())
    adj_list[a].append((b,l))
    adj_list[b].append((a,l))

visited = [0] * (n+1)

def dijkstra(start):
    distance[start] = 0
    pq = [(0, start)]
    
    while pq:
        curr_dist, curr_node = heapq.heappop(pq)

        if distance[curr_node] < curr_dist:
            continue

        for next_node, cost in adj_list[curr_node]:
            new_dist = curr_dist + cost

            if distance[next_node] > new_dist:
                distance[next_node] = new_dist
                heapq.heappush(pq, (new_dist, next_node))
answer = 0
for i in range(1, n+1):
    partial_sum = 0
    distance = [float('inf')]* (n+1)
    dijkstra(i)
    for j in range(1, n+1):
        if distance[j] <= m:
            partial_sum += item[j-1]
    answer = max(answer, partial_sum)

print(answer)