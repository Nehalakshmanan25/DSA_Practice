class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class singlyLl:
    def __init__(self):
        self.head = None

    def insertAtEnd(self, data):
        newNode = node(data)
        if self.head is None:
            self.head = newNode
            return
        currentNode = self.head
        while currentNode.next is not None:
            currentNode = currentNode.next
        currentNode.next = newNode

    def search(self,value):
        if(self.head is None):
            return -1
        curr = self.head
        pos = 0
        while curr is not None:
            if curr.data == value:
                return pos
            curr = curr.next
            pos +=1
        return -1


    def traversal(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
        print("End")

a = singlyLl()
a.insertAtEnd(1) 
a.insertAtEnd(2) 
a.insertAtEnd(3) 
a.insertAtEnd(4) 
output = a.search(3)
print("Value found at index:", output)
