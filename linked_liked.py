class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, val=None):
        self.root = Node(val)
        self.temp = self.root
        self.size = 1
    
    def add(self, val):
        self.temp.next = Node(val)
        self.temp = self.temp.next
        self.size += 1
    
    def pop(self, ind=None):
        if ind >= self.size:
            raise Exception("Index out of range")
        self.size -= 1
        if ind == 0:
            val = self.root.val
            self.root = self.root.next
            return val
        temp = self.root
        for i in range(ind-1):
            temp = temp.next
        val = temp.next.val
        temp.next = temp.next.next
        return val
    
    def popitem(self, val):
        temp = self.root
        ind = 0
        while temp.val != val:
            temp = temp.next
            ind += 1
        return self.pop(ind)

    def __str__(self):
        list = []
        a = self.root
        while a:
            list.append(a.val)
            a = a.next
        return str(list)

l = LinkedList(1)
l.add(2)
l.add(3)
l.add(4)
l.add(5)
l.add(6)
print(l)
print(l.pop(0))
print(l.popitem(5))
print(l)