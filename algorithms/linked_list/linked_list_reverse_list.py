from linked_list_traversal import linked_list_traversal_recursive
from linked_list import Node

a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")

a.next_node = b
b.next_node = c
c.next_node = d

# None -> A -> B -> C -> D -> None
# C A B

def linked_list_reverse_list(node : Node)-> Node:
    current_node = node
    stack = []
    
    while current_node.next_node:
        stack.append(current_node)
        current_node = current_node.next_node

    new_head = current_node

    while stack:
        stack_item = stack.pop()
        current_node.next_node = stack_item
        current_node = stack_item

    current_node.next_node = None

    return new_head

def linked_list_reverse_list_recursive(node : Node)-> Node:    
    previous : Node = None # None
    current = node# A
    while current:
        next = current.next_node # B

        current.next_node = previous
        previous = current
        current = next

    return previous

linked_list_traversal_recursive(linked_list_reverse_list_recursive(a))
