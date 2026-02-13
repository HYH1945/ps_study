import sys

input = sys.stdin.readline

# 일반적인 경우 : 모든 간선을 INF로 초기화
# 벨만포드 : 1번째 라운드 : 간선 1개 거리 노드 최단거리 확정
# 2번째 라운드 : 간선 2개 거리 노드 최단거리 확정
# n-1번째 라운드 : 간선 n-1개 거리 노드 최단거리 확정
# 이므로 n-1 라운드까지 돌았다면 모든 노드의 최단거리가 확정됨
# 예외 경우는 음수 사이클이 존재하는 경우

def bellman_ford():
    distance = [0] * (n + 1) # 모든점이 0 : 시작점을 모든 점으로 설정후 음수사이클만 탐색

    for i in range(n):
        for now in range(1, n + 1):
            for v, weight in adj_list[now]:
                if distance[v] > distance[now] + weight: 
                    distance[v] = distance[now] + weight #최단경로 갱신
                    if i == n - 1: # 음수사이클이 없다면 n-1번까지 돌렸다면 n번째 라운드에서는 갱신이 일어나지 않아야하는데(벨만포드 특징), n번째 라운드에서 갱신이 일어났다는 건
                        return True # 음수사이클 존재
    return False


TC = int(input())

# 음수 가중치가 있는 directed weighted graph
# 도로는 undirected, 웜홀은 directed
# 음수사이클 탐지 문제

answer =[]

for _ in range(TC):
    n, m, w = map(int, input().split())
    adj_list = [[] for _ in range(n+1)]
    minus = False # 음수사이클 있는가?
    for _ in range(m): # 도로 정보 입력
        s, e, t = map(int, input().split())
        adj_list[s].append((e, t))
        adj_list[e].append((s, t))
    for _ in range(w): # 웜홀 정보 입력
        s, e, t = map(int, input().split())
        adj_list[s].append((e, -t))
    if(bellman_ford()):
        answer.append("YES")
    else:
        answer.append("NO")
    
for item in answer:
    print(item)