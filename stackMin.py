class Stack():
    def __init__(self):
         self.arr = []
         self.mins = []
         self.localMin =  None

    def push(self, num):
        self.arr.append(num)
        if self.mins and num > self.mins[-1]: 
            self.mins.append(self.mins[-1])
        else: 
            self.mins.append(num)

    def pop(self):
        a = self.arr.pop()
        self.mins.pop()
        return a

    def min(self):
        return self.mins[-1]

    def __repr__(self):
        return ' '.join([str(i) for i in self.arr])

s = Stack()
s.push(3)
s.push(2)
s.push(1)

print s
print s.min()
s.pop()
print s.min()
s.pop()
print s.min()

