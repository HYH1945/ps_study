import sys
input = sys.stdin.readline

n, m = map(int, input().split())

truth = list(map(int, input().split()))
party = []
for _ in range(m):
    party.append(list(map(int, input().split())))
    