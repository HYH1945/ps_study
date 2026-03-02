import sys
input = sys.stdin.readline

n = int(input())

num = list(map(int,input().split()))

num_set = sorted(list(set(num)))

num_dict = {}
order = 0
for item in num_set:
    num_dict.update({item : order})
    order += 1

answer = []
for item in num:
    answer.append(num_dict.get(item))

for item in answer:
    print(item, end = " ")