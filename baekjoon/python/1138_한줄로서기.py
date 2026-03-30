import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

answer = [0] * len(arr)

for i in range(n):
    count = arr[i]

    for j in range(n):
        if answer[j] == 0:
            if count == 0:
                answer[j] = i+1
                break
            else:
                count -= 1

for item in answer:
    print(item, end = " ")