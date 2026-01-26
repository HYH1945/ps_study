import sys
import heapq

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())

pq = []
min_item = float('inf')

# pq의 최상위 : 가장 큰조각
# 가장 작은조각 : min_item
for item in arr:
    heapq.heappush(pq, (-item, item, 1)) # pq (지금 조각의 무게, 해당 조각의 원래 무게, 지금까지 자른 횟수)
    min_item = min(min_item, item)



diff = -pq[0][0] - min_item # pq[0] : 최상위 pq 원소, pq[0][0] : 조각무게

for _ in range(m):
    max_item, original, count = heapq.heappop(pq)
    max_item = -max_item

    #자르기, 이때 꼭 절반으로 자른다는 조건이 없음 -> 등분이 유리
    count += 1
    new_item = original / count

    min_item = min(min_item, new_item)
    heapq.heappush(pq, (-new_item, original, count))

    diff = min(diff, -pq[0][0] - min_item)

print(diff)