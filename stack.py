class Stack:
    def __init__(self, *values):
        self.values = list(values)
    
    def push(self, val):
        self.values.append(val)
    
    def pop(self):
        if self.values:
            popped = self.values.pop()
            return popped
        raise Exception("Stack is empty")
    
    def __str__(self):
        return str(self.values)

s = Stack(1,2,3,4)
print(s.pop())
print(s.pop())
print(s.pop())
s.push(3)
print(s.pop())
s.push(3)
s.push(3)
print(s)
