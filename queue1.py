class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_nodes = 0

    def size(self):
        return self.num_nodes
    
    def enqueue(self, value): # We are introducing a new node. 
        new_node = Node(value)

        if self.head is None: # Handles if the queue is empty
            # self.head = new_node 
            # self.tail = new_node
            self.head = self.tail = new_node # Same as above two lines. Multiple assingment operator
                # All the attributes or variables in this statement will be given the same value
        else:
            self.tail.next = new_node
            self.tail = new_node # Previous tail is now linkes to the new node. New node is new tail.
        
        self.num_nodes += 1 # Incrementation by 1

    def dequeue(self): # To remove a node from the head of the sequence
        if self.head is None:
            return None # And returning its value. The difference is in the stack the head contained the node
                        # that was added last. In queue, is contains the item that was added first.
        
        #dequeue_node = self.head.value # Not returning the node, only the node's value.
        dequeue_node_value = self.head # Now its returning node with the value.
        self.head = self.head.next
        self.num_nodes -= 1
        return dequeue_node_value
    
q = Queue() # Instantiating a queue obeject from the class. Use enqueue to add items
q.enqueue('a')
q.enqueue('b')
q.enqueue('c')

print("Pass" if (q.size() == 3) else "Fail")
q.enqueue('d')
print("Pass" if (q.size() == 4)else "Fail")

print("Pass" if (q.dequeue() == 'a')else "Fail")
print("Pass" if (q.dequeue() == 'd') else "Fail")
print("Pass" if (q.size() == 2) else "Fail")                                                                                                                                                                                                                                                                                                                       