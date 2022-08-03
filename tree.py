class Node:
    def __init__(self, val=0):
        self.val = val
        self.children = []

    def __str__(self):
        if self.children:
            return f"{self.val} -> {[str(i) for i in self.children]}"
        else:
            return str(self.val)

class Tree:
    def __init__(self, val):
        self.root = Node(val)
        
    def add(self, val, parent=None):
        if parent:
            self.find(parent).children.append(Node(val))
        else:
            self.root.children.append(Node(val))
    
    def find(self, val, temp=None):
        if temp is None:
            temp = self.root
        if temp.val == val:
            return temp
        def inner(node:Node, val):
            if node.val == val:
                return True
            for ch in node.children:
                if inner(ch, val):
                    return ch
            return False
        return inner(temp, val)
    


t = Tree(10)
t.add(11)
t.add(12)
t.add(13)
t.add(22, 11)
t.add(54, 22)
print(t.find(10))