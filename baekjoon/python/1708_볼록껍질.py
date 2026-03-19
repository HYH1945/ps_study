import sys, math
input = sys.stdin.readline

# Convex Hull - Graham's Scan
# 먼저 점들 입력받고 정렬 << 반시계정렬

# 시작점 직선 두점 (first, second) 잡고 시작
# 바로 다음점(next) 고르고
# first, second가 이루는 직선에 대해 왼쪽에 있는지 오른쪽에 있는지 검사

n = int(input())
points = []

for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

def dist(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 )

def ccw(p1, p2, p3):
    # p1, p2가 이루는 직선 기준으로 p3이 어느쪽에 있는지 반환 : 음수는 왼쪽, 양수는 오른쪽, 0은 세 점이 일직선 (문제에선 일단 일직선 경우는 없음)
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

#초기점
points.sort(key=lambda p: (p[1], p[0]))
p0 = points[0]

#초기 반시계방향 정렬 : 초기점과 이루는 각도가 작은 순서대로(아크탄젠트)
points[1:] = sorted(points[1:], key=lambda p: (math.atan2(p[1]-p0[1], p[0]-p0[0]), dist(p0, p)))


# 시작 : 첫번째점, 두번째점 직선 초기상태로 시작
stack = [points[0], points[1]]
for i in range(2,n):
    while len(stack) >= 2:
        second = stack[-1]
        first = stack[-2]

        if(ccw(first, second, points[i]) > 0 ): # points[i] : 추가할지말지 고려
            break # 볼록점 추가를 위해 break
        else:
            stack.pop() # 오목하므로 2번째점은 못쓰는점이니 pop

    stack.append(points[i]) # 볼록점 추가

#print(stack)
print(len(stack))