import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
k = int(input())

board = [[0] * (n) for _ in range(n)]

for _ in range(k):
    row, col = map(int,input().split())
    board[row-1][col-1] = 1

l = int(input())
move = {}
for _ in range(l):
    time, angle = input().split()
    time = int(time)

    move.update({time : angle})

board[0][0] = -1
direction = 1 # 0-북 1-동 2-남 3-서
time = 0
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
queue = deque()
queue.append((0, 0))
curr_row = 0
curr_col = 0

while(True):
    time += 1

    next_row = curr_row + dy[direction]
    next_col = curr_col + dx[direction]

    if 0 <= next_row < n and 0 <= next_col < n:
        queue.append((next_row, next_col))
        if board[next_row][next_col] == 0:
            release = queue.popleft()
            board[release[0]][release[1]] = 0
        elif board[next_row][next_col] == -1:
            break
            
        board[next_row][next_col] = -1
    else:
        break
    
    curr_row, curr_col = queue[-1]

    if move.get(time) == "D":
        direction = (direction + 1) % 4 
    elif move.get(time) == "L":
        direction = (direction + 3) % 4

print(time)