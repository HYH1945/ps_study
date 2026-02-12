import sys

input = sys.stdin.readline

N = int(input())

arr = list(map(int,input().split()))

# two pointer
# 또는 이진탐색 (첫번째 용액을 정한 뒤(총 N회) 두번째 용액을 이진탐색으로 찾기)
start = 0
end = N-1

minimum = float('inf')
result = []
while(True):
    partial_sum = arr[start] + arr[end]
    if abs(partial_sum) < minimum:
        minimum = abs(partial_sum)
        result = [arr[start], arr[end]]

    # 최솟값 갱신되도 계속 포인터 이동 진행해야함 (무한루프)
    if partial_sum > 0:
        end -= 1
    elif partial_sum < 0:
        start += 1
    else: # 0
        result = [arr[start], arr[end]]
        break
    if start == end:
        break

for item in result:
    print(item, end= " ")

