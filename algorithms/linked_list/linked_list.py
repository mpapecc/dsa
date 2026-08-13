class Node:
    data = None
    next_node : Node = None

    def __init__(self, data):
        self.data = data

    def set_next_node(self, next_node):
        self.next_node = next_node

class LinkedList:
    head : Node = None

    def __init__(self, head : Node = None):
        self.head = head

    def prepend(self, node : Node):
        if self.head is None:
            self.head = node
        else:
            node.next_node = self.head
            self.head = node

    def append(self, node : Node):
        if self.head is None:
            self.head = node

        current = self.head

        while current.next_node:
             current = current.next_node

        current.next_node = node

    def __repr__(self):
        if self.head is None:
            print("[]")
        else:
            current = self.head
            while current:
                if(current is self.head):
                    print(f"Head {current.data}")
                elif current.next_node is None:
                    print(f"Tail {current.data}")
                else:
                    print(f"Node {current.data}")
                current = current.next_node
        

# l = LinkedList()

# l.prepend(Node(10))
# l.prepend(Node(20))
# l.prepend(Node(30))
# l.__repr__()


        