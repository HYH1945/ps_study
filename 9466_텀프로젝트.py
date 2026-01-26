import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

#SCC, 사이클탐지

def solve():
    n = int(input())
    adj_list = [[] for _ in range(n+1)]
    arr = list(map(int, input().split()))
    
    for i in range(len(arr)):
        adj_list[i+1].append(arr[i])
    
    visited = [0] * (n+1)
    finished = [0] * (n+1)
    count = 0

    def dfs(start):
        nonlocal count
        visited[start] = True
        for i in adj_list[start]:
            if not visited[i]:
                dfs(i)
            elif not finished[i]:
                temp = i
                while temp != start:
                    count += 1
                    temp = adj_list[temp][0]
                count += 1
        finished[start] = True
    
    for i in range(1, n+1):
        if not visited[i]:
            dfs(i)
    print(n - count)

t = int(input())
for _ in range(t):
    solve()