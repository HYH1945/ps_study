import sys
from itertools import combinations

# 조합 또는 백트래킹

input = sys.stdin.readline

n, m = map(int, input().split())
house = []
chicken = []

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 1:
            house.append((i, j))
        elif row[j] == 2:
            chicken.append((i,j))

selected_chicken = list(combinations(chicken, m)) # 모든 치킨집중 M개 선택한 모든 경우의 수 리스트

result = float('inf')

for combination in selected_chicken: # M개를 선택한 경우의 수 모두 고려
    partial_dist = 0
    for i in range(len(house)):
        min_dist = float('inf')
        house_y, house_x = house[i]
        for j in range(len(combination)): 
            chicken_y, chicken_x = combination[j]
            curr_dist = abs(chicken_y - house_y) + abs(chicken_x - house_x)
            if curr_dist < min_dist:
                min_dist = curr_dist
        partial_dist += min_dist
    
    # 현재 케이스에서 총 거리 계산한 것과 이전에 계산된 최소값과 비교해 갱신
    result = min(result, partial_dist) 
print(result)
