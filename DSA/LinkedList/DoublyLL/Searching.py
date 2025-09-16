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
            print(temp.data,end = " ")
            temp=temp.next
            
    def searching(self,value):
        count = 0 
        temp = self.head
        while(temp is not None):
            if (temp.data == value):
                print("\nValue found at index:", count)
                return
            temp = temp.next
            count +=1
        return -1
                
     
a1=Doubly()
a1.insertAtEnd_m2(10)
a1.insertAtEnd_m2(20)
a1.insertAtEnd_m2(30)
a1.insertAtEnd_m2(40)
a1.insertAtEnd_m2(50)
a1.forwardTraversal()
a1.searching(30)