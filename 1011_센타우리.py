import sys
import math

input = sys.stdin.readline

t = int(input())

x_y_location = []

for i in range(t):
    x, y = map(int, input().split())
    x_y_location.append((x,y))

move = (-1, 0, 1)

#각각 케이스에 대해 계산

# 시작과 끝은 항상 1 / 1
# 서로 인접하는 점끼리는 -1 , 0, +1 관계
# 규칙성이 있는가?
# 16 : 1 2 3 4 3 2 1 #최대 이동거리 4: 16에서부터 나타남
# 15 : 1 2 3 3 3 2 1
# 14 : 1 2 3 3 2 2 1
# 13 : 1 2 3 3 2 1 1 # max : 3,  max^2 + max = 12 < dist -> 2*max+1 : 7
# 12 : 1 2 3 3 2 1
# 11 : 1 2 3 2 2 1
# 10 : 1 2 3 2 1 1 최대 이동거리가 1 늘어난시점에서 다음 케이스는 이동거리가 1 늘어남 : dist > max^2이면 count = 2 * max
# 9 : 1 2 3 2 1 cnt : 5, 최대 이동거리 3 : 9에서부터 나타남 dist == max^2 이면 count = 2 * max - 1
# 8 : 1 2 2 2 1 cnt : 5  이때 최대 이동거리는 2인뎅,,
# 7 : 1 2 2 1 1 cnt : 5  max^2 + max < dist 이면 2 * max + 1?
# 6 : 1 2 2 1   cnt : 4  max^2 < dist 이면 cnt는 2 * max
# 5 : 1 2 1 1   cnt : 4
# 4 : 1 2 1     cnt : 3 #최대 이동거리 2: 4에서부터 나타남, max = dist의 제곱근의 정수부분
# 3 : 1 1 1     cnt : 3
# 2 : 1 1       cnt : 2
# 1 : 1         cnt : 1

answer = []

for item in x_y_location:
    dist = item[1] - item[0]
    max = int(math.sqrt(dist))

    if (max ** 2 == dist):
        count = 2 * max - 1
    elif(max ** 2 + max < dist):
        count = 2 * max + 1
    elif(max ** 2 < dist):
        count = 2 * max
    answer.append(count)

for item in answer:
    print(item)