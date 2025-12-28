import sys
import heapq

# 또 다익스트라

input = sys.stdin.readline

n = int(input())
m = int(input())

adj_list = [[] for _ in range(n+1)]

for i in range(m):
    a, b, c = map(int, input().split())
    adj_list[a].append((b,c)) # b : 목적지, c: cost

# 각 정점을 시작점으로 다익스트라 n번 시행 - 반환
def dijkstra(start):
    pq = []
    distance = [float('inf')] * (n+1)

    distance[start] = 0 # 시작점
    heapq.heappush(pq, (0, start))

    while pq:
        dist, now = heapq.heappop(pq) # dist = 지금까지 온 비용, now : 현재 위치
        if distance[now] < dist:
            continue
        
        for i in adj_list[now]: # i[0] : 도착지, i[1] : cost
            cost = dist + i[1] # 해당 점까지 가는 비용
            if cost < distance[i[0]]: # 해당 점까지 가는 비용이 기존 비용보다 저렴한경우
                distance[i[0]] = cost
                heapq.heappush(pq, (cost, i[0])) # 해당 점을 시작점으로 다시 삽입

    # 못 가는경우 0으로 출력
    for i in range(len(distance)):
        if distance[i] == float('inf'):
            distance[i] = 0
    return distance

answer = []

for i in range(1, n+1):
    answer.append(dijkstra(i))

for j in range(n):
    for k in range(1, n+1):
        print(answer[j][k], end=" ")
    print()

