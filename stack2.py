class Stack: # Because we are not using a linked list, no need to define a node class.
    def __init__(self): # Give it a constructor method and in it, set up an attribute call items.
        self.items = []
    
    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.size() == 0:
            return None
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

print("Pass" if (stack.size() == 5) else "Fail")
stack.push(5)
print("Pass" if (stack.size() == 5) else "Fail")

print("Pass" if (stack.pop() == 5) else "Fail")
print("Pass" if (stack.pop() == 4) else "Fail")