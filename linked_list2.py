class Node:
    def __init__(self, value): # Basic implementation of a linked list.
        self.value = value
        self.next = None # None is a special value in Python that denotes the lack of value.

# How to loop or traverse through a linked list.
def iter_linked_list(node):
    while node is not None: # Is best practice to use "is" instead of == when testing against a null value.
        print(node.value)
        node = node.next

head = Node("1st Node") # Head is the value, Next is the null value, the end of the sequence.
head.next = Node("2nd Node")
head.next.next = Node("3rd Node")

iter_linked_list(head)
