import sys
from collections import deque

input = sys.stdin.readline

N,M = map(int,input().split())

adj_list = [[] for _ in range(N+1)]
arr = []
for _ in range(M):
    arr.append(list(map(int,input().split())))
indegree = [0] * (N+1)

for i in range(M):
    for j in range(1, len(arr[i]) - 1):
        adj_list[arr[i][j]].append(arr[i][j+1])
        indegree[arr[i][j+1]] += 1

def topological_sort():
    result = []
    queue = deque()

    for i in range(1, N+1):
        if indegree[i] == 0:
            queue.append(i)
    
    while queue:
        curr = queue.popleft()
        result.append(curr)

        for next in adj_list[curr]:
            indegree[next] -= 1
            if indegree[next] == 0:
                queue.append(next)
    return result

result = topological_sort()

if len(result) < N:
    print(0)
else:
    for item in result:
        print(item)

# khan 식


# reverselist = []
# visited = [0] * (N+1)
# def topologicalsort(start):
#     visited[start] = True
#     for i in adj_list[start]:
#         if not visited[i]:
#             topologicalsort(i)
#     reverselist.append(start)

# for i in range(1, N+1):
#     if not visited[i]:
#         topologicalsort(i)

# reverselist.reverse()

# if len(reverselist) == 0:
#     print(0)
# else:
#     for item in reverselist:
#         print(item)