import sys
input = sys.stdin.readline

#DP

arr = list(map(int, input().split()))

left = 0
right = 0
count = 0
for item in arr:
#     #print(count)
#     if item == 0:
#         break
#     if item == left or item == right:
#         count += 1
#     else:
#         if left == 0:
#             left = item
#             count += 2
#         elif right == 0:
#             right = item
#             count += 2
#         else:
#             if item % 2 == 1: # 가야하는 곳이 홀수
#                 if left % 2 == 0: # 왼발이 짝수에 있음
#                     left = item
#                     count += 3
#                 elif right % 2 == 0: # 오른발이 짝수에 있음
#                     right = item
#                     count += 3
#                 else: # left, right 모두 홀수이고, item이랑 같지 않으면 건너뛰는 방법밖에 없
#                     left = item
#                     count += 4
#             else: # 가야하는 곳이 짝수
#                 if left % 2 == 1: # 왼발이 홀수에 있음
#                     left = item
#                     count += 3
#                 elif right % 2 == 1: # 오른발이 홀수에 있음
#                     count += 3
#                 else:
#                     left = item
#                     count += 4

# print(count)