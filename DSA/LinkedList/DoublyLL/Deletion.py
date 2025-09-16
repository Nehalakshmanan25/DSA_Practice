class Node:
    def __init__(self,data,prev=None,next=None):
        self.data = data
        self.prev = prev
        self.next = next
class Doubly:
    head = None
    tail = None
        
    def insertAtEnd_m2(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            return
        self.tail.next = newNode
        newNode.prev = self.tail
        self.tail = newNode
        
    def forwardTraversal(self):
        if self.head is None:
            print("List is empty")
        temp = self.head
        print("Forward Traversal")
        while temp is not None:
            print(temp.data, end = " ")
            temp=temp.next
            
    def deleteAtStart(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next
        self.head.prev = None
        
    def deleteAtEnd(self):
        if self.head is None:
            print("List is empty")
            return
        self.tail = self.tail.prev
        self.tail.next = None
        
    def deleteAtMiddle(self,pos):
        if self.head is None:
            print("List is empty")
            return
        if pos ==0:
            self.head = self.head.next
        curr = self.head
        count = 0 
        before = None
        
        if curr is not None and count < pos:
            before = curr
            curr = curr.next
            count +=1
        before.next = curr.next
        curr.next.prev = before
                 
a1=Doubly()
a1.insertAtEnd_m2(10)
a1.insertAtEnd_m2(20)
a1.insertAtEnd_m2(30)
a1.insertAtEnd_m2(40)
a1.insertAtEnd_m2(50)
a1.deleteAtStart()
a1.deleteAtEnd()
a1.deleteAtMiddle(1)
a1.forwardTraversal()


        