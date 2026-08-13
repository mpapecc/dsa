from linked_list_traversal import linked_list_traversal_recursive
from linked_list import Node

a = Node("A")
b = Node("B")
c = Node("C")


a.next_node = b
b.next_node = c

q = Node("Q")
r = Node("R")
s = Node("S")

q.next_node = r 
r.next_node = s

# None(p) -> A(c) -> B(n) -> C -> D -> None
# C A B

def linked_list_zipper_lists(head1 : Node, head2: Node)-> Node:
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    current1 = head1
    current2 = head2

    while current1 and current2:
        next1 = current1.next_node
        next2 = current2.next_node

        current1.next_node = current2
        current2.next_node = next1

        current1 = next1
        current2 = next2

    return head1


linked_list_traversal_recursive(linked_list_zipper_lists(a, q))
