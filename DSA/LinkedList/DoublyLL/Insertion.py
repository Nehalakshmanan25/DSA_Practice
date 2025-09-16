class Node:
    def __init__(self,data,prev=None,next=None):
        self.data = data
        self.prev = prev
        self.next = next
class Doubly:
    head = None
    tail = None
    
    def insertAtStart(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            return
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode
        
    def insertAtMiddle(self,data,pos):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        count = 0
        curr = self.head
        while (curr is not None and count < pos-1):
            curr = curr.next
            count +=1
        if curr is None or curr.next is None:
            self.insertAtEnd_m2(data)
            return
        curr.next.prev = newNode
        newNode.prev = curr
        curr.next = newNode
        newNode.prev = curr
            
    def insertAtEnd_m1(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = newNode
        newNode.prev = temp
        self.tail = newNode
        
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
            
    def backTraversal(self):
        if self.head is None:
            print("List is empty")
        temp = self.head
        print("\nBackward Traversal")
        temp = self.tail
        while temp is not None:
            print(temp.data, end = " ")
            temp=temp.prev
            
a1=Doubly()
a1.insertAtStart(10)
a1.insertAtStart(20)
a1.insertAtMiddle(5000,3)
a1.insertAtEnd_m1(30)
a1.insertAtEnd_m2(40)
a1.forwardTraversal()
a1.backTraversal()