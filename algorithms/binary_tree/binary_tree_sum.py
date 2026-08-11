from binary_tree import Node, tree

def binary_tree_sum(node: Node) -> int:
    if node is None:
        return 0

    return binary_tree_sum(node.left_node) + node.value + binary_tree_sum(node.right_node)

print(binary_tree_sum(tree.root))
