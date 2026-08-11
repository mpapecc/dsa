from binary_tree import Node, tree

def binary_tree_traverse(node: Node) -> list[int]:
    if node is None:
        return []

    return binary_tree_traverse(node.left_node) + [node.value] + binary_tree_traverse(node.right_node)


print(binary_tree_traverse(tree.root))
