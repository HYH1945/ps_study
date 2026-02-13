import sys

input = sys.stdin.readline

str_1 = " " + (input().rstrip())
str_2 = " " + (input().rstrip())

dp = [[0 for col in range(len(str_2))] for row in range(len(str_1))]

for i in range(len(str_1)):
    for j in range(len(str_2)):
        if i == 0 or j == 0:
            dp[i][j] = 0
        elif str_1[i] == str_2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

answer = []


curr_x = len(str_1) - 1
curr_y = len(str_2) - 1

while(curr_x > 0 and curr_y > 0):
    if dp[curr_x][curr_y] == dp[curr_x][curr_y - 1]:
        curr_y -= 1
    elif dp[curr_x][curr_y] == dp[curr_x-1][curr_y]:
        curr_x -= 1
    else: # 대각선 갈때 append
        answer.append(str_1[curr_x])
        curr_y -= 1
        curr_x -= 1
        if dp[curr_x][curr_y] == 0:
            break
print(len(answer))

if(len(answer) != 0):
    print("".join(reversed(answer)))