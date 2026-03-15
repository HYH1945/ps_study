import sys

input = sys.stdin.readline

string = input().rstrip()
boom = input().rstrip()

stack = []
count = 0

for item in string:
    stack.append(item)

    # 역순으로 올라가며 비교
    # if len(stack) >= len(boom):
    #     for i in range(len(boom)):
    #         if stack[len(stack) - i - 1] == boom[len(boom)-i - 1]:
    #             count += 1
    #     if count == len(boom):
    #         for j in range(count):
    #             stack.pop()
    #     count = 0
    
    if len(stack) >= len(boom):
        if ''.join(stack[-len(boom):]) == boom: #join : high cost
            for _ in range(len(boom)):
                stack.pop()

if len(stack) == 0:
    print("FRULA")
else:
    print("".join(stack))