import sys
import heapq
input = sys.stdin.readline


# 1~N
# 가능한한 작은문제 먼저풀기
# 단, 먼저푸는것이 좋은문제가 있는경우 그문제를 먼저 풀어야함
# 4 < 2 / 3 < 1 인 경우
n, m = map(int, input().split())


adj_list = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    indegree[b] += 1

pq = []

# 맨첨에 갈수있는놈중 가장 작은놈부터 
for i in range(1, n+1):
    if indegree[i] == 0:
        heapq.heappush(pq, i)
result = []
while pq:
    now = heapq.heappop(pq)
    result.append(now)

    for next in adj_list[now]:
        indegree[next] -= 1
        if indegree[next] == 0:
            heapq.heappush(pq, next)

for item in result:
    print(item, end = " ")

# 1->2->3->4
# ^  ^  |
# |  ㄴ----|
# |_____|

# 1부터 N까지 순서대로 가리키게 연결하고,
# priority 시작점부터 전부 dfs 돌리고
# 나머지 모든점에 대해 낮은점부터 !visited 조건으로 dfs 방문
# 방문순서 기록
# (틀림)

# 선행문제는 인접리스트로 기록,
# 진입차수를 노드마다 기록하고,
# 1부터 n까지 진입차수가 0인놈부터 minPQ에 넣어서
# 하나씩 꺼내면서 방문
# 이때 인접한 곳이 있다면 지금 문제를 풀고 접근할 수 있는
# 문제라는 뜻이므로 그 인접한곳의 차수를 1뺌
# 결국 진입차수가 0이면 지금 접근할 수 있는곳



