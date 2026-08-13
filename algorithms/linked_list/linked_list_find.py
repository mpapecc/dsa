from linked_list import Node

a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")

a.next_node = b
b.next_node = c
c.next_node = d


def linked_list_find(node : Node, target : str):
    while node:
        if target == node.data:
            return True
        node = node.next_node

    return False

def linked_list_find_recursive(node : Node, target : str):
    if node is None:
        return False

    if node.data == target:
        return True

    return linked_list_find_recursive(node.next_node, target)

print(linked_list_find_recursive(a, "C"))