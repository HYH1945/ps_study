import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())

adj_list = [[] for _ in range(N+1)]

spanning = [[] for _ in range(N+1)]

pq = []

for i in range(M):
    u, v, w = map(int, input().split())
    adj_list[u].append((v,w))
    adj_list[v].append((u,w))
    heapq.heappush(pq, (w, u, v))
visited = [0] * (N+1)

def prim():
    answer = 0
    count = 0
    max_edge = 0
    while pq:
        weight, start, end = heapq.heappop(pq)
        
        if not visited[end]:
            #print(start, end)
            visited[end] = True
            answer += weight
            count += 1
            spanning[start].append((end, weight))
            max_edge = max(max_edge, weight)
            
        
        elif not visited[start]:
            #print(start, end)
            visited[start] = True
            answer += weight
            count += 1
            spanning[end].append((start, weight))
            max_edge = max(max_edge, weight)
        if count == N:
            break

    print(answer)
    return answer - max_edge

print(prim())

# 2,5 3,2 5,1 6,4 6,7


# (1,3) (1,6) (2,5) (2,1) (3,2) (6,4)

