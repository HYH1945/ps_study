import sys
input = sys.stdin.readline

r, c, t = map(int, input().split())

matrix = []
cleaner = []

for i in range(r):
    row = list(map(int, input().split()))
    matrix.append(row)

    if row[0] == -1:
        cleaner.append(i)


# 1. 미세먼지 확산

for _ in range(t):
    temp_matrix = [[0 for col in range(c)] for row in range(r)]
    for i in range(r):
        for j in range(c):
            if matrix[i][j] > 0:
                amount = matrix[i][j] // 5
                count = 0
                for dx, dy in [(0,1), (0,-1), (-1,0), (1,0)]:
                    next_row, next_col = i+dy, j+dx
                    if 0 <= next_row < r and 0 <= next_col < c and matrix[next_row][next_col] != -1:
                        temp_matrix[next_row][next_col] += amount
                        count += 1
                matrix[i][j] -= amount * count
    for i in range(r):
        for j in range(c):
            matrix[i][j] += temp_matrix[i][j]


    # 2. 공기청정기
    top = cleaner[0]
    bottom = cleaner[1]

    # 위 공기청정기 순환
    for i in range(top - 1, 0, -1): matrix[i][0] = matrix[i-1][0]
    for i in range(c - 1): matrix[0][i] = matrix[0][i+1]
    for i in range(top): matrix[i][c-1] = matrix[i+1][c-1]
    for i in range(c - 1, 1, -1): matrix[top][i] = matrix[top][i-1]
    matrix[top][1] = 0

    # 아래 공기청정기 순환
    for i in range(bottom + 1, r - 1): matrix[i][0] = matrix[i+1][0]
    for i in range(c - 1): matrix[r-1][i] = matrix[r-1][i+1]
    for i in range(r - 1, bottom, -1): matrix[i][c-1] = matrix[i-1][c-1]
    for i in range(c - 1, 1, -1): matrix[bottom][i] = matrix[bottom][i-1]
    matrix[bottom][1] = 0
        
answer = 0
for i in range(r):
    answer += sum(matrix[i])

print(answer + 2)