import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    start, end = map(int, input().split())

    arr.append((end, start))

arr.sort()
progress = 0
answer = 0
for item in arr:
    end, start = item[0], item[1]

    if progress <= start:
        progress = end
        answer += 1

print(answer)
