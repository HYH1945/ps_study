import sys
input = sys.stdin.readline

n, m = map(int, input().split())

adj_list = [[] for _ in range(n+1)]
for _ in range(m):
    u,v = map(int,input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

count = 0

visited = [0] * (n+1)
def dfs(node, parent):
    visited[node] = parent

    for i in adj_list[node]:
        if not visited[i]:
            dfs(i, parent)

for i in range(1, n+1):
    if visited[i] == 0:
        dfs(i, i)

visited = set(visited)

print(len(visited) -1 )