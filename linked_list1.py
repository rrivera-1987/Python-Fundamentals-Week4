class Node:
    def __init__(self, value): # Basic implementation of a linked list.
        self.value = value
        self.next = None # None is a special value in Python that denotes the lack of value.

head = Node("1st Node") # Head is the value, Next is the null value, the end of the sequence.
head.next = Node("2nd Node")
head.next.next = Node("3rd Node")

print(head.value)
print(head.next.value)
print(head.next.next.value) # This is how you would access different indices in a linked list.