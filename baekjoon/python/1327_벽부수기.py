import sys
from collections import deque

# 최단 횟수 : bfs (각 시행에 weight가 없을때)

input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(input().split())
answer = sorted(arr)
# visited set, key를 문자열로


# bfs
# 배열을 각각 자리바꾼 결과를 queue에 넣고 반복
def solve():
    visited = set(["".join(arr)]) 
    queue = deque()
    queue.append((arr, 0))
    while(queue):
        curr_arr, count = queue.popleft()
        if curr_arr == answer:
            return count

        for i in range(n-k+1):
            # curr_arr 변경하면 반복문돌면서 다음 반복에도 영향을 주므로 메모리 독립적으로 관리해야함
            next_arr = curr_arr[:i] + curr_arr[i:i+k][::-1] + curr_arr[i+k:]
            next_arr_str = "".join(next_arr)
            if next_arr_str not in visited:
                visited.add(next_arr_str)
                queue.append((next_arr, count + 1))
    return -1

print(solve())