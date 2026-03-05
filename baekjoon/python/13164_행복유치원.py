import sys
input = sys.stdin.readline

# greedy
# 가장 차이 작은애끼리

n, k = map(int,input().split())

children = list(map(int, input().split()))

diff = [0] * (n-1)
for i in range(n-1):
    diff[i] = children[i+1] - children[i]

diff.sort()
answer = 0
for i in range(n-k):
    answer += diff[i]

print(answer)