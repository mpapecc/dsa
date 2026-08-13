from linked_list import LinkedList, Node

a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")

a.next_node = b
b.next_node = c
c.next_node = d


def linked_list_sum(linkedList : LinkedList):
    result = []
    node = linkedList.head
    while node:
        result.append(node.data)
        node = node.next_node

    return result

def linked_list_traversal_recursive(node : Node):
    if(node is None):
        return

    print(node.data)
    linked_list_traversal_recursive(node.next_node)

# print(linked_list_traversal_recursive(a))