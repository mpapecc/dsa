from binary_tree import BinaryTree, Node


def print_tree(tree : BinaryTree):
    lines, *_ = _build_tree_string(tree.root)
    print('\n'.join(lines))

def print_tree_from_node(node : Node):
    lines, *_ = _build_tree_string(node)
    print('\n'.join(lines))


def _build_tree_string(node: Node):
    """
    Returns (lines, width, height, middle) where:
    - lines: list of strings representing this subtree
    - width: total width of the box
    - height: number of lines
    - middle: horizontal position of this node's label within the box
    """
    if node is None:
        return [], 0, 0, 0

    line = str(node.value)
    width = len(line)

    # Leaf node
    if node.left_node is None and node.right_node is None:
        return [line], width, 1, width // 2

    # Only left child
    if node.right_node is None:
        lines, n, p, x = _build_tree_string(node.left_node)
        s = x + 1
        u = width - x - 1
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + line
        second_line = x * ' ' + '/' + (n - x - 1 + width) * ' '
        shifted_lines = [line + u * ' ' for line in lines]
        return [first_line, second_line] + shifted_lines, n + width, p + 2, n + width // 2

    # Only right child
    if node.left_node is None:
        lines, n, p, x = _build_tree_string(node.right_node)
        s = x + 1
        u = width - x - 1
        first_line = line + x * '_' + (n - x) * ' '
        second_line = (width + x) * ' ' + '\\' + (n - x - 1) * ' '
        shifted_lines = [u * ' ' + line for line in lines]
        return [first_line, second_line] + shifted_lines, n + width, p + 2, width // 2

    # Two children
    left, n, p, x = _build_tree_string(node.left_node)
    right, m, q, y = _build_tree_string(node.right_node)
    first_line = (x + 1) * ' ' + (n - x - 1) * '_' + line + y * '_' + (m - y) * ' '
    second_line = x * ' ' + '/' + (n - x - 1 + width + y) * ' ' + '\\' + (m - y - 1) * ' '

    if p < q:
        left += [n * ' '] * (q - p)
    elif q < p:
        right += [m * ' '] * (p - q)

    zipped_lines = zip(left, right)
    lines = [first_line, second_line] + [a + width * ' ' + b for a, b in zipped_lines]
    return lines, n + m + width, max(p, q) + 2, n + width // 2