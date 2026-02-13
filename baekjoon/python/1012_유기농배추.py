import sys
from collections import deque

input = sys.stdin.readline

t = int(input())


for _ in range(t):
    m, n, k = map(int ,input().split())
    farm = [[0 for col in range(m)] for row in range(n)]
    
    seed_list = []
    for _ in range(k):
        col, row = map(int, input().split())
        farm[row][col] = 1
        seed_list.append((row, col))
    #print(farm)
    def bfs(row, col):
        queue = deque()
        dx = [0, 0, -1, 1]
        dy = [1, -1, 0, 0]
        farm[row][col] = -1
        queue.append((row, col))

        while queue:
            r, c = queue.popleft()
            for i in range(4):
                if 0 <= r + dy[i]< n and 0 <= c + dx[i] < m:
                    if farm[r+dy[i]][c+dx[i]] == 1:
                        farm[r+dy[i]][c+dx[i]] = -1
                        queue.append((r+dy[i], c+dx[i]))

    answer = 0 
    for seed_row, seed_col in seed_list:
        if farm[seed_row][seed_col] == 1:
            bfs(seed_row , seed_col)
            answer += 1
    
    
    print(answer)
