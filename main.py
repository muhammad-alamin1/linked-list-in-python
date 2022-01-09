from linked_list import *
from doubly_linked_list import *

if __name__ == '__main__':
    sll = LinkedList()
    dll = DoublyLinkedList()


    def test_append():
        assert dll.head.next is None, "linked list is empty, so head should point to Node"

        item = 5
        dll.append(item)
        assert dll.head.next.data is item, 'head should point to the first node'

        second_item = 9
        dll.append(second_item)
        assert dll.head.next.data == item, 'head should point to the first node'

        first_node = dll.head.next
        second_node = first_node.next
        assert first_node.next.data == second_item, 'first node should point to second node'

        assert second_node.prev.data == item, 'Previous node of second node should be the first node'
        assert str(dll) == '5,8', 'string representation of dll should match 5, 8'


    def test_prepend():
        assert dll.head.next is None, "linked list is empty, so head should point to Node"

        item = 2
        dll.prepend(item)
        assert dll.head.next.data is item, 'head should point to the first node'


    print(dll)
