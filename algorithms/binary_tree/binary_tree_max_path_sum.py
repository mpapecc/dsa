from binary_tree import Node, tree
#                     50
#                  /      \
#                30         70
#               /  \       /  \
#             20    40    60   80
#            /  \   /
#           10  25 35

def binary_tree_max_path_sum(node: Node):
    if(node is None):
        return float("-inf")

    if node.right_node is None and node.left_node is None:
        return node.value
    
    leftMax = binary_tree_max_path_sum(node.left_node)
    rightMax = binary_tree_max_path_sum(node.right_node)

    sum = node.value + max(leftMax, rightMax);
    return sum

print(binary_tree_max_path_sum(tree.root))

