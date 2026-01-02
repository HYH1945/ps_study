import sys
sys.setrecursionlimit(100000)

input = sys.stdin.readline

n = int(input())

adj_list = [[] for _ in range(n+1)]
for i in range(n):
    line = list(map(int,input().split()))
    j = 1
    while(True):
        if line[j] == -1:
            break
        adj_list[line[0]].append((line[j], line[j+1]))
        adj_list[line[j]].append((line[0], line[j+1]))
        j += 2

# 시작점 찾기

visited = [-1] * (n+1)
def dfs(start, dist):
    for v, w in adj_list[start]:
        if visited[v] == -1:
            visited[v] = w + dist
            dfs(v, dist + w)

visited[1] = 0
dfs(1,0)

max_dist = 0
start = -1
for i in range(1, len(visited)):
    if max_dist < visited[i]:
        max_dist = visited[i]
        start = i

visited = [-1] * (n+1)
visited[start] = 0

dfs(start, 0)

print(max(visited))