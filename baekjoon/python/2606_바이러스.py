import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

adj_list = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

visited = [0] * (n+1)
order = 1

def dfs(start):
    global order
    visited[start] = order
    order += 1
    for i in adj_list[start]:
        if not visited[i]:
            dfs(i)

dfs(1)

print(max(visited)-1)