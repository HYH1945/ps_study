import sys
sys.setrecursionlimit(20000)

input = sys.stdin.read # 입력에 EOF 나타내는 표시가 없어서 한번에 다 읽어야할듯

class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

class BST:
    def __init__(self, root):
        self.root = root
    
    def insert(self, value):
        self.curr = self.root
        while(1):
            if value < self.curr.item:
                if self.curr.left != None:
                    self.curr = self.curr.left
                else:
                    self.curr.left = Node(value)
                    break
            else:
                if self.curr.right != None:
                    self.curr = self.curr.right
                else:
                    self.curr.right = Node(value)
                    break
    
    def search(self, value):
        self.current_node = self.root
        while self.current_node:
            if self.current_node.item == value:
                return True
            elif self.current_node.item > value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right
        return False
    
    def post_order(self, node):
        if node:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.item)


nums = input().split()
if nums:
    root_val = int(nums[0])
    bst = BST(Node(root_val))

    for i in range(1, len(nums)):
        bst.insert(int(nums[i]))

    bst.post_order(bst.root)

#bst.post_order(bst.root)