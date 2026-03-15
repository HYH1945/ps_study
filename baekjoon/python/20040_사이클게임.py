import sys
sys.setrecursionlimit(500000)

input = sys.stdin.readline

#union find

n, m = map(int, input().split())
parent = [i for i in range(n)]
def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)
    
    if rootX != rootY:
        if rootX > rootY:
            parent[rootY] = rootX
        else:
            parent[rootX] = rootY
        return True #사이클 x
    return False # 사이클 o
result = 0
for i in range(m):
    u, v = map(int,input().split())
    if result == 0:
        if union(parent, u, v) == False:
            result = i+1

print(result)

#visited = [0] * n
# def cycle_detect(start):
#     visited[start] = True
#     for i in adj_list[start]:
#         if not visited[i]:
#             cycle_detect(i)
#         if i != start and visited[i]:
#             return 1
#     return 0


    