import sys
input = sys.stdin.readline

arr = []

for _ in range(9):
    arr.append(list(map(int,input().rstrip())))

# 1. 행 검사
# 2. 열 검사
# 3. 3*3 박스 검사

def possible(a, b, value):
    #print("TEST")
    for i in range(9):
        if arr[a][i] == value:
            return False
    for j in range(9):
        if arr[j][b] == value:
            return False
    
    a_idx = a//3 + 3
    b_idx = b//3 + 3

    for i in range(a_idx):
        for j in range(b_idx):
            if arr[i][j] == value:
                return False
    return True

zeros = [(i,j) for i in range(9) for j in range(9) if arr[i][j] == 0] # 0인 위치를 담은 배열 [(i,j)] 식으로 저장
def solve(idx):
    if idx == len(zeros):
        for item in arr:
            print("".join(map(str, item)))
        return

    r, c = zeros[idx]
    for k in range(1,10):
        if possible(r,c,k):
            arr[r][c] = k
            solve(idx + 1)

            # 실패시 백트래킹
            arr[r][c] = 0

solve(0)
