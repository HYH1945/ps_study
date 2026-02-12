import sys
import heapq

N, K = map(int, input().split())

adj_list = [[] for _ in range(N+1)]
for _ in range(K):
    A,B,C = map(int, input().split())
    adj_list[A].append((B,C))
    adj_list[B].append((A,C))

def prim(start):
    pq = [(0, start)]
    visited = [0] * (N+1)
    
    total_weight = 0
    count = 0
    maximum_edge = 0

    while pq:
        w, v = heapq.heappop(pq)

        if not visited[v]:
            visited[v] = True
            count += 1
            total_weight += w

            maximum_edge = max(maximum_edge, w)
            if count == N:
                break

            for vertex, weight in adj_list[v]:
                if not visited[vertex]:
                    heapq.heappush(pq, (weight, vertex))
    return total_weight - maximum_edge

print(prim(1))