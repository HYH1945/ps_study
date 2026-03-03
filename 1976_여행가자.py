import sys
input = sys.stdin.readline
n = int(input())
m = int(input())

adj_list = [[] for _ in range(n+1)]
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(len(row)):
        if row[j] == 1:
            adj_list[i+1].append(j+1)
            adj_list[j+1].append(i+1)

order = list(map(int, input().split()))

visited = [0] * (n+1)

def dfs(start):
    visited[start] = 1

    for i in adj_list[start]:
        if not visited[i]:
            dfs(i)

dfs(order[0])
for item in order:
    if visited[item] == 0:
        print("NO")
        exit(0)
print("YES")