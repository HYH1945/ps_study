import sys
input = sys.stdin.readline

# 재귀 딕셔너리

n = int(input())
food_list = []
for _ in range(n):
    save = list(input().split())
    save.pop(0)
    food_list.append(save)
    
root = 0

home = {}

for foods in food_list:
    curr_node = home
    for food in foods:
        if food not in curr_node:
            curr_node[food] = {}
        curr_node = curr_node[food]


def print_home(curr_node, depth):
    for food in sorted(curr_node.keys()):
        print('--' * depth + food)
        print_home(curr_node[food], depth + 1)
    
print_home(home, 0)