import sys
input = sys.stdin.readline

n, m = map(int, input().split())

tree = list(map(int,input().split()))

high = max(tree)
low = 0

while(low <= high):
    mid = (low + high)//2

    total = 0
    for item in tree:
        if item > mid:
            total += (item - mid)
    
    if total >= m: # 너무 길게자름
        result = mid 
        low = mid + 1
    else:  # 너무 짧게자름
        high = mid - 1
    
print(result)