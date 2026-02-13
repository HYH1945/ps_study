import sys
input = sys.stdin.readline

N, S = map(int, input().split())

arr = list(map(int,input().split()))

# two pointer

# 첫번째 문제 : 이진탐색으로 접근함(실패) -> 투포인터
# 두번째 문제 : sum을 사용함 (계속 전체합을 새로구해서 시간초과 실패) -> 직접 하나씩 더하기
# 세번째 문제점 : 문제를 잘못읽음. 부분합이 S"이상"도 다 고려해야함


def solve():
    first = 0
    last = 0
    minimum = float("inf")
    current_sum = 0
    while(True):
        if current_sum >= S:
            minimum = min(minimum, last-first)
            current_sum -= arr[first]
            first += 1
        elif last == N:
            break
        else:
            current_sum += arr[last]
            last += 1

    return 0 if minimum == float('inf') else minimum

print(solve())
# 이진탐색? (원래 배열을 수정안한상태에서 찾아야해서 쓰면안됨)

#arr.sort()
# aim = S
# first = arr[0]
# last = arr[-1]
# size = len(arr)
# middle = arr[size // 2]
# result = []

# while(True):
#     if middle == aim:
#         result.append(middle)
#         break

#     # elif aim > last:
#     #     result.append(last)
#     #     continue

#     elif aim > middle: # 오른쪽
#         if aim > last:
#             result.append(last)
#             aim -= last
#             continue
#         size //= 2
#         first = arr[size] #middle
#         middle = arr[size + (size//2)]
#         continue

#     elif aim < middle: # 왼쪽 
#         size //= 2
#         last = arr[size - 1]
#         middle = arr[size//2]
#         continue

# print(len(result))