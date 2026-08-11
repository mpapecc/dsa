from binary_tree import Node, tree

#                     50
#                  /      \
#                30         70
#               /  \       /  \
#             20    40    60   80
#            /  \   /
#           10  25 35

def binary_tree_dfs(node: Node, value : int) -> bool:
    if node is None:
        return False

    stack : list[Node] = [node]
    while stack:
        current = stack.pop()
        print(current.value)
        if current.value == value:
            return True
        if current.right_node : stack.append(current.right_node)
        if current.left_node : stack.append(current.left_node)

    return False

print(binary_tree_dfs(tree.root, 25))
