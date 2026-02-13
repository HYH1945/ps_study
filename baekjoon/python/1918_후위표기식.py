import sys

input = sys.stdin.readline

expression = input().rstrip()

stack = []
answer = []
priority = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}

# 스택에 삽입하면서 스택 top의 연산자 우선순위 고려할 때, 본인이랑 우선순위가 같은경우에도 pop 다 때리고 넣어야한다는걸 간과했따 

for item in expression:
    if 'A' <= item <= 'Z':
        answer.append(item)
    elif item == '(':
        stack.append(item)
    elif item == ')':
        while(stack):
            removed = stack.pop()
            if removed == '(':
                break
            answer.append(removed)
    else: # 연산자
        while(stack and priority[item] <= priority[stack[-1]]):
            answer.append(stack.pop())
        stack.append(item)

while(stack):
    answer.append(stack.pop())

for item in answer:
    print(item, end ='')