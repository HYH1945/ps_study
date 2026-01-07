import sys
input = sys.stdin.readline

# greedy로 풀면 안됨 (예외가 있음)
# 왼쪽부터 차근차근 뜯어나가는 경우로 풀이 : DP


# ex) sticker_list[0][1] : 0행 1열의 스티커를 뜯었을때 나올 수 있는 최대 점수

T = int(input())
answer = []

for _ in range(T):
    n = int(input())
    sticker_list = []
    for _ in range(2):
        sticker_list.append(list(map(int, input().split())))
    
    if n == 1:
        print(max(sticker_list[0][0], sticker_list[1][0]))
        continue

    # 1번째 열까지 최적의 해는 대각선에 위치한 스티커 하나 뜯는 경우 한가지
    sticker_list[0][1] += sticker_list[1][0]
    sticker_list[1][1] += sticker_list[0][0]

    for i in range(2, n):
        sticker_list[0][i] += max(sticker_list[1][i-1], sticker_list[1][i-2]) # 대각선 (왼쪽밑)에 있던걸 뜯은경우 / 대각선(왼쪽밑)의 왼쪽에 있던걸 뜯은경우
        sticker_list[1][i] += max(sticker_list[0][i-1], sticker_list[0][i-2]) # 대각선 (왼쪽위)에 있던걸 뜯은경우 / 대각선(왼쪽위)의 왼쪽에 있던걸 뜯은경우
    
    answer.append(max(sticker_list[0][n-1], sticker_list[1][n-1]))

for item in answer:
    print(item)

    # while(1):
    #     curr_max = max( max(sticker_list[0]), max(sticker_list[1]) )
    #     if curr_max == -1:
    #         break
    #     for i in range(n):
    #         if sticker_list[0][i] == curr_max:
                
    #             # 스티커 떼기
    #             sum += sticker_list[0][i]

    #             sticker_list[0][i] = -1   

    #             # 뗀 스티커의 오른쪽
    #             if i != len(sticker_list[0]) - 1:
    #                 sticker_list[0][i+1] = -1 

    #             # 뗀 스티커의 왼쪽
    #             if i != 0:
    #                 sticker_list[0][i-1] = -1 
                
    #             # 뗀 스티커의 아래쪽
    #             sticker_list[1][i] = - 1
    #             break

    #         elif sticker_list[1][i] == curr_max:
    #             # 스티커 떼기
    #             sum += sticker_list[1][i]
    #             sticker_list[1][i] = -1   

    #             # 뗀 스티커의 오른쪽
    #             if i != len(sticker_list[1]) - 1:
    #                 sticker_list[1][i+1] = -1 

    #             # 뗀 스티커의 왼쪽
    #             if i != 0:
    #                 sticker_list[1][i-1] = -1 
                
    #             # 뗀 스티커의 위쪽
    #             sticker_list[0][i] = -1
    #             break
    
    #answer.append(sum)

