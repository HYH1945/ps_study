import sys
from collections import deque

# 지도 크기가 최대 8*8이고, 벽 3개를 무조건 지어야함,
# 벽세우는 최악의 경우의수가 64C3이므로 브루트포스, (이때 벽3개 세우고 다시 원복하는 백트래킹 필요 또는 itertools.combination)
# 다 세워보고 bfs

input = sys.stdin.readline

n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

max_safety_zone = 0
#print(arr)
def bfs():
    queue = deque()
    temp_graph = [row[:] for row in arr]
    #print(temp_graph)
    for i in range(n):
        for j in range(m):
            if temp_graph[i][j] == 2:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0<= ny < m:
                if temp_graph[nx][ny] == 0:
                    temp_graph[nx][ny] = 2
                    queue.append((nx, ny))
        
    safety_zone = 0
    for i in range(n):
        for j in range(m):
            if temp_graph[i][j] == 0:
                safety_zone += 1
    
    global max_safety_zone
    max_safety_zone = max(max_safety_zone, safety_zone)

def build_wall(count):
    if count == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                arr[i][j] = 1
                build_wall(count+1)
                arr[i][j] = 0

build_wall(0)
print(max_safety_zone)