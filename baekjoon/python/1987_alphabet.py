import sys
input = sys.stdin.readline

r, c = map(int, map(int, input().split()))
board = []
for _ in range(r):
    board.append(list(input().rstrip()))


visited = [0] * 26
answer = 0
def dfs(row, col, count):
    global answer
    answer = max(answer, count)
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    for i in range(4):
        next_row = row + dy[i]
        next_col = col + dx[i]

        if (0 <= next_row < r and 0 <= next_col < c):
            alphabet_idx = ord(board[next_row][next_col]) - ord('A') 
            if not visited[alphabet_idx]:
                visited[alphabet_idx] = True
                dfs(next_row, next_col, count + 1)
                visited[alphabet_idx] = False

visited[ord(board[0][0]) - ord('A')] = True                
dfs(0, 0, 1)
print(answer)
