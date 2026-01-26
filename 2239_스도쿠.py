import sys
input = sys.stdin.readline

#백트래킹, 3*3 박스 체크 복습

arr = []
for _ in range(9):
    arr.append(list(map(int, input().rstrip())))

zero = [(i,j) for i in range(9) for j in range(9) if arr[i][j] == 0]

def possible(row, col, value):
    
    # 행 열 체크
    for i in range(9):
        if arr[row][i] == value or arr[i][col] == value:
            return False
    

    # 3*3 박스 체크 (인덱스 주의)
    row_idx = (row//3) * 3
    col_idx = (col//3) * 3

    
    for i in range(row_idx,row_idx + 3):
        for j in range(col_idx, col_idx + 3):
            if arr[i][j] == value:
                return False
    
    return True

def solve(idx):
    if idx == len(zero):
        for row in arr:
            print("".join(map(str, row)))

        exit(0) #  return말고 exit으로 프로그램 종료
    
    row, col = zero[idx]
    for i in range(1, 10):
        if possible(row, col, i):
            arr[row][col] = i
            solve(idx+1)
            
            #실패시
            arr[row][col] = 0 

solve(0)
