import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    items = list(input().rstrip())
    stack = []
    answer = "YES"
    for item in items:
        if item == '(':
            stack.append(item)
        elif item == ')':
            if len(stack) != 0:
                stack.pop()
            else:
                answer = "NO"
                break
    
    if len(stack) != 0:
        answer = "NO"
    print(answer)
