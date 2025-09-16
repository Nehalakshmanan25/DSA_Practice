class Stack:
    def __init__(self):
        self.value = []
    
    def is_empty(self):
        return len(self.value) == 0
        
    def push(self,item):
        return self.value.append(item)
        
    def Pop(self):
        if self.is_empty():
            return None
        return self.value.pop()
        
    def topValue(self):
        if self.is_empty():
            return None
        return self.value[-1]
        
    def sizeOfStack(self):
        return len(self.value)
    
    def display(self):
        print(self.value)
a = Stack()
a.push(10)
a.push(20)
a.push(30)
a.push(40)
a.push(50)
print("This value is popped:", a.Pop())
print("This is the top value:", a.topValue())
print("The size of the stack", a.sizeOfStack())
a.display()

