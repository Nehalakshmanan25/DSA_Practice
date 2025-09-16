class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class singlyLl:
    def __init__(self):
        self.head = None

    def insertAtStart(self, data):
        newNode = node(data)
        newNode.next = self.head
        self.head = newNode
    def deleteAtStart(self):
        if (self.head is None):
            print("List is empty")
            return
        self.head = self.head.next

    def deleteAtEnd(self):
        if (self.head is None):
            print("List is empty")
            return
        if self.head.next is None:
            self.head =None
            return 
        current = self.head
        prev = None
        while current.next is not None:
            prev = current
            current = current.next
        prev.next = None
    
    def deleteAtMiddle(self,position):
        if (self.head is None):
            print("EMPTY")
            return
        if position == 0:
            self.head = self.head.next
            return
        curr = self.head
        prev =None
        count = 0 
        while curr is not None and count < position:
            prev = curr 
            curr = curr.next
            count +=1
        if curr is None:
            print("Change the position it is larger")
            return
        prev.next = curr.next 

    def traversal(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
        print("End")

a = singlyLl()
a.insertAtStart(0) 
a.insertAtStart(1)     
a.insertAtStart(2)  
a.insertAtStart(3)  
a.insertAtStart(4)  
a.insertAtStart(5)   
a.deleteAtStart()
a.deleteAtEnd() 
a.deleteAtMiddle(1)
a.traversal()       
