import sys
from collections import Counter

# 부분배열 (인덱스가 연속인 부분합)

sys = sys.stdin.readline

t = int(input())
n = int(input())

A = list(map(int,input().split()))

m = int(input())
B = list(map(int,input().split()))

sum_A = []

for i in range(n):
    sum = 0
    for j in range(i, n):
         sum += A[j]
         sum_A.append(sum)

sum_B = []
for i in range(m):
    sum = 0
    for j in range(i, m):
        sum += B[j]
        sum_B.append(sum)

counter_B = Counter(sum_B)

# A의 모든 부분합 체크 -> 목표 T까지 필요한 합은 T - 부분합(A), 이 부분이 B의 부분합에 존재하는가?

need = 0
answer = 0
for item in sum_A:
    need = t - item
    if need in counter_B:
        answer += 1

print(answer)