``
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

# kosaraju or tarjan
# unweighted directed graph

# kosaraju : topological sort
# 1. 逆graphの topological orderを探す。
# 2. その順でdfs(countを上がって)

v, e = map(int, input().split())
adj_list = [[] for _ in range(v+1)]
adj_list_reversed = [[] for _ in range(v+1)]

for _ in range(e):
    A, B = map(int,input().split())
    adj_list[A].append(B)
    adj_list_reversed[B].append(A)

visited = [0] * (v+1)
reverselist = []

def topologicalsort(v, arr):
    visited[v] = True
    for i in arr[v]:
        if not visited[i]:
            topologicalsort(i, arr)
    reverselist.append(v) # もう訪問する点が無い

# 1. 逆graphの topological orderを探す。
for i in range(1, v+1):
    if not visited[i]:
        topologicalsort(i, adj_list_reversed)
reverselist.reverse()

visited = [0] * (v+1)
id = [0] * (v+1)
count = 1

def dfs(v, arr, count):
    visited[v] = True
    id[v] = count
    for i in arr[v]:
        if not visited[i]:
            dfs(i, arr, count)

for i in reverselist:
    if not visited[i]:
        dfs(i, adj_list, count)
    count += 1
#print(id)

id_set = set(id)
id_set.remove(0)

print(len(id_set))
for item in id_set:
    for j in range(v+1):
        if id[j] == item:
            print(j, end=" ")
    print(-1)
