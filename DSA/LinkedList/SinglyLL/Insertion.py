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

    def insertAtEnd(self, data):
        newNode = node(data)
        if self.head is None:
            self.head = newNode
            return
        currentNode = self.head
        while currentNode.next is not None:
            currentNode = currentNode.next
        currentNode.next = newNode

    def insertAtMiddle(self, position, data):
        newNode = node(data)

        if position == 0:
            newNode.next = self.head
            self.head = newNode
            return

        currentNode = self.head
        count = 0

        while currentNode.next is not None and count < position - 1:
            currentNode = currentNode.next
            count += 1
        newNode.next = currentNode.next
        currentNode.next = newNode

    def traversal(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
        print("End")

a = singlyLl()
a.insertAtStart(0) 
a.insertAtStart(-1)     
a.insertAtMiddle(3, 1)   
a.insertAtEnd(2) 
a.traversal()   