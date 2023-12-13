class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def append(self, value):
        new_node = DoubleNode(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            print("Head Node created:", self.head.value)
            return
    
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        print("Appended new Node with Value: ", self.tail.value)

dlist = DoublyLinkedList()
dlist.append("First Node")

# Opening a file with -i means that the code in the files has been run and is in memory
# we are in the program and able to interact with it.