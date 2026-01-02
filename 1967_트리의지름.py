import sys
import heapq
sys.setrecursionlimit(10000) # recursionerror 뜸 (기본 최대 1000회라)

# greedy로 풀었는데 틀림
# 핵심 : 스타트 노드 고르기 : 어떤 노드를 고르든 거기서 가장 먼 곳에 있는 노드를 구하면 해당 노드가 지름의 양끝점 노드중 하나가 튀어나옴

input = sys.stdin.readline

n = int(input())

#max pq
pq = []

adj_list = [[] for _ in range(n+1)]
for i in range(n-1):
    u, v, w = map(int, input().split())
    adj_list[u].append((v, w))
    adj_list[v].append((u, w))

visited = [-1] * (n+1) # 방문안했다면 -1, 방문했다면 그외
def dfs(curr, dist):
    for next, weight in adj_list[curr]:
        if(visited[next] == -1):
            visited[next] = dist + weight
            dfs(next, dist + weight) # 그 다음 방문하는 정점 거리는 현재까지 온 거리를 더함

visited[1] = 0
dfs(1,0) # visited배열에 1로 부터 모든 방문거리 나올 것
# 시작점 (지름의 양끝점중 하나) 찾기
dist = -1
start = 1
for i in range(1, len(visited)):
    if dist < visited[i]:
        dist = visited[i]
        start = i
 
# 다시 그 시작점으로 dfs로 가장 먼 정점 거리 구하면 끝
visited = [-1] * (n+1)

visited[start] = 0
dfs(start, 0)
print(max(visited))



# greedy로 푼건데 틀렸으니 무시

# start_weight, start_vertex = heapq.heappop(pq)
# start_weight = -start_weight
# start_vertex = -start_vertex

# visited = [0] * (n+1)
# answer = 0

# def dfs(start, answer):

#     visited[start] = True
#     pq = []
#     for v, w in adj_list[start]:
#         heapq.heappush(pq, (-w,-v))
#     while(1):
#         if not pq:
#             return start
#         weight, vertex = heapq.heappop(pq)
#         weight = -weight
#         vertex = -vertex
#         if(visited[vertex] == False):
#             answer += weight
#             break
#     dfs(vertex, answer)

