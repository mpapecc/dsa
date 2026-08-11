from binary_tree import Node, tree

#                     50
#                  /      \
#                30         70
#               /  \       /  \
#             20    40    60   80
#            /  \   /
#           10  25 35

def binary_tree_min_value(node: Node) -> bool:
    if node is None:
        return 0
    min_value = float("inf")
    stack : list[Node] = [node]
    while stack:
        current = stack.pop()
        min_value = min(current.value, min_value);
        if current.right_node : stack.append(current.right_node)
        if current.left_node : stack.append(current.left_node)

    return min_value

def binary_tree_min_value_recursion(node: Node) -> bool:
    if node is None:
        return float("inf")

    leftMin = binary_tree_min_value_recursion(node.left_node)
    rightMin = binary_tree_min_value_recursion(node.right_node)

    return min(leftMin, node.value, rightMin)

print(binary_tree_min_value_recursion(tree.root))
