import sys

input = sys.stdin.readline

N = int(input())

arr = list(map(int,input().split()))
arr.sort()

minimum = float('inf')

for i in range(N-2):
    # arr[i] 한개 고정, 나머지 두개는 left right 범위조절 (two pointer)
    left = i+1
    right = N-1
    while(True):
        current_sum = arr[i] + arr[left] + arr[right]

        if abs(current_sum) < minimum:
            minimum = abs(current_sum)
            result = [arr[i], arr[left], arr[right]]

        if current_sum < 0:
            left += 1
        elif current_sum > 0:
            right -= 1 
        else:
            result = [arr[i], arr[left], arr[right]]
            break

        if left == right:
            break

for item in result:
    print(item, end = " ")