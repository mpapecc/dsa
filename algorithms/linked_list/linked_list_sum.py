from linked_list import LinkedList, Node

a = Node(2)
b = Node(8)
c = Node(3)
d = Node(7)

a.next_node = b
b.next_node = c
c.next_node = d


def linked_list_sum(node : Node):
    count = 0

    while node:
        count += node.data
        node = node.next_node

    return count

def linked_list_sum_recursive(node : Node):
    if node == None:
        return 0

    return node.data + linked_list_sum_recursive(node.next_node) 

print(linked_list_sum_recursive(a))