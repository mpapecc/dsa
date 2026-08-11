from binary_tree import Node, tree

#                     50
#                  /      \
#                30         70
#               /  \       /  \
#             20    40    60   80
#            /  \   /
#           10  25 35

def binary_tree_bfs(node: Node, value : int) -> bool:
    if node is None:
        return False

    queue : list[Node] = [node]

    while queue:
        current = queue.pop(0)
        print(current.value)
        if current.value == value:
            return True

        if current.right_node : queue.append(current.right_node)
        if current.left_node : queue.append(current.left_node)

    return False


print(binary_tree_bfs(tree.root, 40))
