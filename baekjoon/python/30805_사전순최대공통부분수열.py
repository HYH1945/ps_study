import sys
input = sys.stdin.readline

n = int(input())
arr_A = list(map(int,input().split()))

m = int(input())
arr_B = list(map(int, input().split()))

answer = []

while(True):
    set_A = set(arr_A)
    set_B = set(arr_B)

    intersect = set_A & set_B

    if not intersect:
        break

    max_val = 0
    for item in intersect:
        max_val = max(item, max_val)

    answer.append(max_val)

    index_A = arr_A.index(max_val)
    index_B = arr_B.index(max_val)

    arr_A = arr_A[index_A + 1:]
    arr_B = arr_B[index_B + 1:]

    if not arr_A or not arr_B:
        break

print(len(answer))
for item in answer:
    print(item, end=" ")