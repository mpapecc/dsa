class Node:
    def __init__(self, value, left_node, right_node):
        self.value = value
        self.left_node = left_node
        self.right_node = right_node

class BinaryTree:
    def __init__(self, root: Node):
        self.root = root

#                     50
#                  /      \
#                30         70
#               /  \       /  \
#             20    40    60   80
#            /  \   /
#           10  25 35

n10 = Node(10, None, None)
n25 = Node(25, None, None)
n35 = Node(35, None, None)
n60 = Node(60, None, None)
n80 = Node(80, None, None)

n20 = Node(20, n10, n25)
n40 = Node(40, n35, None)
n70 = Node(70, n60, n80)

n30 = Node(30, n20, n40)
n50 = Node(50, n30, n70)

tree = BinaryTree(n50)

#                     1
#                  /      \
#                1         2
#               /  \       /  \
#              1    2     3    4
#            /  \   /
#           1    2  3