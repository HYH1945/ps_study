import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

grid = []
cheese = []

for r in range(n):
    item = list(map(int, input().split()))
    grid.append(item)
    for c in range(m):
        if item[c] == 1:
            cheese.append((r,c))

# 외부공간 찾기, visited[row][col] == 0이면 내부공간
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
visited = [[0] * m for _ in range(n)]
def bfs():
    queue = deque()
    queue.append((0,0))
    visited[0][0] = 1
    while queue:
        row, col = queue.popleft()
        for i in range(4):
            next_row = row + dy[i]
            next_col = col + dx[i]
            if 0 <= next_row < n and 0 <= next_col < m:
                if grid[next_row][next_col] == 0 and visited[next_row][next_col] == 0:
                    queue.append((next_row,next_col))
                    visited[next_row][next_col] = 1

time = 0
while(cheese):
    visited = [[0] * m for _ in range(n)]
    bfs()
    
    remove_bin = []
    for c_row, c_col in cheese:
        count = 0
        
        # 치즈에 인접한 상하좌우 체크
        for i in range(4):
            next_c_row = c_row + dy[i]
            next_c_col = c_col + dx[i]

            if 0 <= next_c_row < n and 0 <= next_c_col < m:
                if visited[next_c_row][next_c_col] == 1: # 외부공간이면
                    count += 1
        
        #녹음
        #Qprint(f'({c_row}, {c_col}) 카운트: {count}')
        if count >= 2:
            grid[c_row][c_col] = 0
            remove_bin.append((c_row, c_col))
            #cheese.remove((c_row, c_col))

    for c_row, c_col in remove_bin:
        cheese.remove((c_row, c_col))
    time += 1
print(time)