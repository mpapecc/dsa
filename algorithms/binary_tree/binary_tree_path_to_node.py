from binary_tree import Node, tree

#                     50
#                  /      \
#                30         70
#               /  \       /  \
#             20    40    60   80
#            /  \   /
#           10  25 35

def binary_tree_path_to_node(node: Node, value : int) -> list[int]:
    if node is None:
        return []

    if node.value == value:
        return [node.value]

    left = binary_tree_path_to_node(node.left_node, value)
    if len(left) > 0:
        return [node.value] + left
    
    right = binary_tree_path_to_node(node.right_node, value)
    if len(right) > 0:
        return [node.value] + right

    return []

print(binary_tree_path_to_node(tree.root, 25))
