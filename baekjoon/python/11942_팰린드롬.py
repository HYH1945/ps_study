import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int,input().split()))

m = int(input())

question = []
for _ in range(m):
    question.append(list(map(int,input().split())))

dp = [[0] * n for _ in range(n)]

# dp[i][j] : i~j 팰린드롬 여부


# 반복문 처리순서 고려를 못해서 이상한답이 나왔음
# 이전계산을 써먹어야 DP지

# 길이 1 처리
for i in range(n):
    dp[i][i] = 1

#길이 2 처리
for i in range(n-1):
    if arr[i] == arr[i+1]:
        dp[i][i+1] = 1
         
#길이 3이상 처리 : 양 끝점 같은지 확인후 그 내부가 팰린드롬이면 팰린드롬임

for k in range(2, n): # k: 구간의 길이 - 1
    for i in range(n - k): 
        
        # 즉 구간의 길이가 3, 4, 5 ~ n까지 늘어나며 구간길이가 3일때를 다채우고 4일때를 채우고 순서로 반복
        # 예시) 첫 루프 : arr[0], arr[2] 비교 -> arr[1], arr[3] 비교
        # 그렇게 구간길이 3짜리를 다 처리했으면 구간길이 4짜리 처리
        # -> arr[0], arr[3] , arr[1], arr[4] ~~~ 쭉
        j = i + k 
        
        if arr[i] == arr[j]:
            if dp[i+1][j-1] == 1:
                dp[i][j] = 1


for item in question:
    print(dp[item[0]-1][item[1]-1])

# 투 포인터 방식은 시간초과 (질문이 여러번 최대 100만번 들어오는게 문제) -> DP로 모든경우의 팰린드롬 먼저 싹계산해두면 질문마다 O(1)임
# def ispalindrome(S, E):
#     S_idx = S-1
#     E_idx = E-1
#     # 홀수
#     if ((E-S) % 2 == 0):
#         half = (S+E) // 2
#         while(True):
#             first = arr[S_idx]
#             last = arr[E_idx]

#             if first != last:
#                 print("0")
#                 break

#             S_idx += 1
#             E_idx -= 1
#             if S_idx == half:
#                 print("1")
#                 break
#     # 짝수
#     else:
#         half = (S+E) // 2
#         while(True):
#             first = arr[S_idx]
#             last = arr[E_idx]
#             if first != last:
#                 print("0")
#                 break
#             S_idx += 1
#             E_idx -= 1

#             # cross
#             if S_idx == (half + 1) or E_idx == half:
#                 print("1")
#                 break


# for item in question:
#     ispalindrome(item[0], item[1])