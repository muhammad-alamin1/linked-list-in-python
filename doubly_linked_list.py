# Create Node
class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __repr__(self):
        return repr(self.data)


class DoublyLinkedList:
    def __init__(self):
        self.head = Node()

    def __repr__(self):
        nodes = []

        current_node = self.head.next
        while current_node:
            nodes.append(repr(current_node))
            current_node = current_node.next

        return ','.join(nodes)

    # add node last index
    def append(self, data):
        new_node = Node(data)

        if self.head.next is None:
            self.head.next = new_node
            return

        current_node = self.head.next
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node
        new_node.prev = current_node

    # add node first index
    def prepend(self, data):
        first_node = self.head.next
        new_node = Node(data, None, first_node)
        self.head.next = new_node

        if first_node:
            first_node.prev = new_node

    # search item
    def search(self, item):
        current_node = self.head.next
        while current_node:
            if current_node.data == item:
                return current_node

            current_node = current_node.next
        return None

    # remove node
    def remove_node(self, node):
        if node.prev:
            node.prev.next = node.next
        else:  # first node
            self.head.next = node.next
        if node.next:
            node.next.prev = node.prev

    # remove item
    def remove(self, item):
        node = self.search(item)
        if node is None:
            return

        self.remove_node(node)

    # insert node
    def insert(self, prev_node, new_data):
        if prev_node is None:
            print(f'This node doesn\' exists in doubly linked list')
            return

        new_node = Node(data=new_data)

        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        if new_node.next is not None:
            new_node.next.prev = new_node


"""Doubly Linked List Complexity 

** The time complexity for initializing a doubly linked list O(1). The space 
   complexity is O(1) as no additional memory is required to initialize the linked list. 
** For insertion at the end, the time complexity is O(n) as we need to traverse to the last element.
** The time complexity for searching a given element in the linked list is O(n) as we have to loop over all 
   the nodes and check for the required one. 
** The time complexity remove method for doubly linked list is O(n)

"""
