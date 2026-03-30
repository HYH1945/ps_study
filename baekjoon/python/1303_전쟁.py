import sys
sys.setrecursionlimit(10**4)

from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())

board = [] 
visited = [[0 for col in range(n)] for row in range(m)]

for _ in range(m):
    board.append(list(input().rstrip()))

max_value = 0
count = 1

def dfs(row, col):
    global count
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    visited[row][col] = count
    
    for i in range(4):
        next_row = row + dy[i]
        next_col = col + dx[i]
        if(0<=next_row<m and 0<=next_col<n and (visited[next_row][next_col] == 0)):
            if board[next_row][next_col] == board[row][col]:
                count += 1
                dfs(next_row, next_col)
    global max_value
    max_value= max(max_value, count)

answer = [0, 0]
for i in range(m):
    for j in range(n):
        if(visited[i][j] == 0):
            max_value = 0
            count = 1
            dfs(i,j)
            if board[i][j] == 'W':
                answer[0] += pow(max_value, 2)
            else:
                answer[1] += pow(max_value, 2)
        
print(answer[0], answer[1])