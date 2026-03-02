import sys
input = sys.stdin.readline

n, r, q = map(int, input().split())

adj_list = [[] for _ in range (n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

# 각 노드를 루트로 잡은 서브트리개수 구해두고 반환

size = [0] * (n+1)
visited = [0] * (n+1)

def count_subtree(curr):
    visited[curr] = True
    size[curr] = 1

    for neighbor in adj_list[curr]:
        if not visited[neighbor]:
            size[curr] += count_subtree(neighbor)
    return size[curr]

count_subtree(r)

for _ in range(q):
    print(size[int(input())])