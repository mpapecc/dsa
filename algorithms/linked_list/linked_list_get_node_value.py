from linked_list import LinkedList, Node

a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")

a.next_node = b
b.next_node = c
c.next_node = d

index = 2

def linked_list_get_node_value(node : Node, index: int):
    current_index = 0

    while current_index < index:
        current_index += 1
        node = node.next_node

    return node.data

def linked_list_get_node_value_recursive(node : Node, index: int):
    if node is None:
        return None

    if index == 0:
        return node.data

    return linked_list_get_node_value_recursive(node.next_node, index - 1)

print(linked_list_get_node_value_recursive(a, index))