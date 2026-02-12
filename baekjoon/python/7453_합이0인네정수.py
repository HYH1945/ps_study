import sys

input = sys.stdin.readline

# 1. A B / C D 두개로 갈라서 각 경우의수의 합을 모두담은 SumAB, SumCD 배열 만들고
# 2. SumAB의 각 item에 대해 반복 -> SumCD에서 -item이 있는가 탐색 (이건 SumCD 배열만 정렬해서 이진탐색하면 될듯) << 시간초과
# 이진탐색이 한번 찾는게 O(logN^2)라 sum_cd의 원소개수(n^2)만큼 루프돌리면 O(n^2logN^2)라 초과난듯함

# New 2. 딕셔너리(hashmap)으로 순회 : sum_ab의 값이 -30, -10, 10, 30, 30 이런식이 있다고 하면
# sum_ab[-30] = 1, sum_ab[-10] = 1, sum_ab[30] = 2 이런식으로 저장되니까, sum_cd의 원소로 인덱스 접근하면 한원소 검색당 O(1)임
# 이때 딕셔너리 get메서드는 해당 키에대한 값이 없으면 키에러 나니까 get(val, 0)으로 값이 없으면 0반환하도록 처리 
# #<< O(1)을 sum_cd의 원소개수(n^2)만큼만 하면됨

# 단 , 이진탐색에 비해 메모리는 많이먹음

# 또 다른 방식 : Two pointer : sum_ab, sum_cd 한 배열에 합치고 양끝점 포인터, 

n = int(input())

a = []
b = []
c = []
d = []

for _ in range(n):
    item_a, item_b, item_c, item_d = map(int, input().split())
    a.append(item_a)
    b.append(item_b)
    c.append(item_c)
    d.append(item_d)


sum_ab = {}
sum_cd = {}

for i in range(n):
    for j in range(n):
        sum_ab[a[i] + b[j]] = sum_ab.get((a[i] + b[j]), 0) + 1


count = 0
for i in range(n):
    for j in range(n):
        target = -(c[i] + d[j])
        if target in sum_ab:
            count += sum_ab[target]
print(count)


# def bin_search(arr, value):
#     start = 0
#     end = len(arr)

#     mid = (end + start) // 2
    
#     while(start < end):
#         mid = (end + start) // 2
#         if arr[mid] == value:
#             return True
#         elif arr[mid] < value:
#             start = mid + 1
#         elif arr[mid] > value:
#             end = mid
#         #print(start, end)
#     return False
# sum_cd.sort()



# count = 0
# for item in sum_ab:
#     if bin_search(sum_cd, -item):
#         count += 1

# print(count)