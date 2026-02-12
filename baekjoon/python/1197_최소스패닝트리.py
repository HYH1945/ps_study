import sys
import heapq

# 변수명 다 다르게 줘야함

input = sys.stdin.readline

v, e = map(int, input().split())
adj_list = [[] for _ in range(v+1)]

for _ in range(e):
    u, v_node, w = map(int, input().split())
    adj_list[u].append((v_node, w))
    adj_list[v_node].append((u, w))

def prim(start):
    pq = []
    visited = [False] * (v+1)
    answer = 0
    cnt = 1

    visited[start] = True
    for vertex, weight in adj_list[start]:
        heapq.heappush(pq, (weight, vertex))

    while pq:
        curr_w, curr_v = heapq.heappop(pq)
        if (visited[curr_v] == False):
            visited[curr_v] = True
            answer += curr_w
            cnt += 1 

            if cnt == v:
                break
            for next_v, next_w in adj_list[curr_v]:
                if not visited[next_v]:
                    heapq.heappush(pq, (next_w, next_v)) 
    
    return answer

answer = prim(1)

print(answer)

