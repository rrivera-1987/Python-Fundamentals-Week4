class Node:
    def __init__(self, value): # Basic implementation of a linked list.
        self.value = value
        self.next = None # None is a special value in Python that denotes the lack of value.

class LinkedList:
    def __init__(self): # a linked list must always know where its head is.
       self.head = None # Set up a constructor method of __init__ with the parameter of self.
    
    def append(self, value): # Value refers to the value we wish to append
        new_node = Node(value) 
        if self.head is None:
            self.head = new_node # new_node will be the head value.
            print("Head Node created: ", self.head.value)
            return 
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = new_node
        print("Appended new Node with value: ", node.next.value)
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            print("Head Node created: ", self.head.value)
            return
        new_node.next = self.head
        self.head = new_node
        print("Prepended new Head Node with value: ", self.head.value)
        print("Node following Head is: ", self.head.next.value)

llist = LinkedList()
llist.prepend("First Node")
llist.prepend("Inserted New First Node")