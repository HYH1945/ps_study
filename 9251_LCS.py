import sys

# Longest Common Subsequence 알고리즘 참고
# Dynamic Programming

input = sys.stdin.readline  

str_1 = " " + input().rstrip() # 인덱스 1부터 문자가 나타나도록 전처리
str_2 = " " + input().rstrip()

# 행 열 인덱스를 잘 신경써야,,
LCS = [[0 for col in range(len(str_2))] for row in range(len(str_1))] 

# dp 구성 (역시 행, 열 인덱스 잘 신경써야,,)
for i in range(len(str_1)): # 행
     for j in range(len(str_2)): # 열
        if i == 0 or j == 0:
            LCS[i][j] = 0
        elif str_1[i] == str_2[j]:
            LCS[i][j] = LCS[i-1][j-1] + 1
        else:
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])

#print(LCS[len(str_1) - 1][len(str_2) - 1])

# 부분 수열 추적
answer = []
curr_x = len(str_1) - 1
curr_y = len(str_2) - 1
while(1):
    if LCS[curr_x][curr_y] == LCS[curr_x][curr_y - 1]: # 왼쪽 탐색
        curr_y = curr_y - 1
    elif LCS[curr_x][curr_y] == LCS[curr_x-1][curr_y]: # 위쪽 탐색
        curr_x = curr_x - 1
    else: #왼쪽과 위쪽 모두 같은 값이 없다면 대각선으로
        answer.append(str_1[curr_x])
        curr_x = curr_x - 1
        curr_y = curr_y - 1
        if LCS[curr_x][curr_y] == 0:
            break

print("".join(reversed(answer)))
