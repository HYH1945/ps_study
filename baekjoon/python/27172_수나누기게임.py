import sys

# 소수판별 (에라토스테네스의 체). 복습필요

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

pos = [False] * (1000001)

for item in arr:
    pos[item] = True

point = [0] * (1000001)

for item in arr:
    # x, 2x, 3x, 4x ,,, check
    for i in range(item * 2, 1000001, item):
        if pos[i]:
            point[item] += 1
            point[i] -= 1

result = []
for item in arr:
    result.append(str(point[item]))

print(" ".join(result))

#  for i in range(len(arr)):
#     for j in range(i+1, len(arr)):
#         if arr[i] % arr[j] == 0:
#             point[i] += 1
#             point[j] -= 1
#         elif arr[j] % arr[i] == 0:
#             point[i] -= 1
#             point[j] += 1
#         #print(arr[i], arr[j], point)

