class HashTable:
    def hash(self, val):
        ascii_sum = sum(ord(i) for i in str(val))
        hash_ = ascii_sum % self.size
        while hash_ in self.dict:
            if self.dict[hash_] == val:
                return hash_
            hash_ += 1
        return hash_
            
    def __init__(self, size=10):
        self.size = size
        self.dict = {}
    
    def add(self, val):
        self.dict[self.hash(val)] = val

    def find(self, val):
        return self.dict[self.hash(val)]

    def __str__(self):
        return str(self.dict)

h = HashTable(1)
h.add(5)
h.add('hello')
h.add('hello')
print(h)