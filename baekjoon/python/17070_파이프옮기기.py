import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

pipe = [0, 1, 0] # 0 : 가로 1: 세로 2: 대각
queue = deque()
queue.append(pipe)

answer = 0

def digonal_check(row, col):
    if matrix[row+1][col] == 1 or matrix[row][col+1] == 1 or matrix[row+1][col+1] == 1:
        return False
    else:
        return True

while queue:
    pipe_end_row, pipe_end_col, pipe_shape = queue.popleft()
    
    if pipe_end_row == n-1 and pipe_end_col == n-1:
        answer += 1

    if pipe_shape == 0:
        if pipe_end_col + 1 < n and matrix[pipe_end_row][pipe_end_col + 1] != 1:
            queue.append([pipe_end_row, pipe_end_col + 1, 0])
        if pipe_end_col + 1 < n and pipe_end_row + 1 < n and digonal_check(pipe_end_row, pipe_end_col) == True:
            queue.append([pipe_end_row + 1, pipe_end_col + 1, 2])
    elif pipe_shape == 1:
        if pipe_end_row + 1 < n and matrix[pipe_end_row + 1][pipe_end_col] != 1:
            queue.append([pipe_end_row + 1, pipe_end_col, 1])
        if pipe_end_col + 1 < n and pipe_end_row + 1 < n and digonal_check(pipe_end_row, pipe_end_col) == True:
            queue.append([pipe_end_row + 1, pipe_end_col + 1, 2])
    else:
        if pipe_end_col + 1 < n and matrix[pipe_end_row][pipe_end_col + 1] != 1:
            queue.append([pipe_end_row, pipe_end_col + 1, 0])
        if pipe_end_row + 1 < n and matrix[pipe_end_row + 1][pipe_end_col] != 1:
            queue.append([pipe_end_row + 1, pipe_end_col, 1])
        if pipe_end_col + 1 < n and pipe_end_row + 1 < n and digonal_check(pipe_end_row, pipe_end_col) == True:
            queue.append([pipe_end_row + 1, pipe_end_col + 1, 2])

print(answer)

