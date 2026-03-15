import sys
input = sys.stdin.readline

n = int(input())

answer = []
for i in range(n):
    age, name = input().split()
    age = int(age)

    answer.append((age, i, name))

answer.sort()

for i in range(len(answer)):
    print(f'{answer[i][0]} {answer[i][2]}')