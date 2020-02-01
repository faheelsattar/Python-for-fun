class Node:
    def __init__(self,value:int):
        self.value=value
        self.next= None
        self.previous= None

class DoubleLinkedList:  
    def __init__(self):
        self.head= None
        self.tail=None
        self.counter=0
    
    def insertAtBeginning(self, value:int):
        node = Node(value)
        if self.head is None:
            self.head=node
            self.tail=node
        else:
            node.next=self.head
            node.previous=None  
            self.head.previous=node
            self.head=node
        self.counter+=1

    def insertAtEnd(self, value:int):
        node = Node(value)
        if self.head is None:
            self.head=node
            self.tail=node
        else:
            tempnode = self.head
            while(tempnode.next):
                tempnode=tempnode.next
            tempnode.next=node
            node.previous=tempnode
            self.tail=node
        self.counter+=1
    
    def insertAtPosition(self, value:int, position:int):
        if position == 1:
            self.insertAtBeginning(value)
        else:
            i=0
            node= Node(value)
            prevnode= self.head
            nextnode= self.head
            while(i!=position-1):
                prevnode=nextnode
                nextnode = nextnode.next
                i+=1
            prevnode.next=node
            node.previous=prevnode
            node.next=nextnode
            nextnode.previous=node
            self.counter+=1
    
    def removeFromBeginning(self):
        tempnode=self.head
        tempnode.previous=None
        nextnode= tempnode.next
        tempnode=None
        self.head=nextnode
        self.counter-=1

    def removeFromEnd(self):
        prevnode= self.head
        nextnode=self.head
        while(nextnode.next):
            prevnode=nextnode
            nextnode= nextnode.next
        prevnode.next=None
        nextnode.previous=None
        self.tail=prevnode
    
    def removeFromPosition(self, position:int):
        if position == 1:
            self.removeFromBeginning()
        elif position == self.counter:
            self.removeFromEnd()
        else:
            i=0 
            prevnode=self.head
            nextnode=self.head
            while (i!=position-1):
                prevnode=nextnode
                nextnode=nextnode.next
                i+=1
            prevnode.next=nextnode.next
            nextnode.next.previous = prevnode
            nextnode=None
            self.counter-=1
    
    def printList(self):
        tempnode=self.head
        while(tempnode):
            print(tempnode.value)
            tempnode=tempnode.next

dll = DoubleLinkedList()

dll.insertAtBeginning(4)
dll.insertAtBeginning(5)
dll.insertAtEnd(98)
dll.insertAtBeginning(6)
dll.insertAtPosition(43,4)

dll.removeFromBeginning()
dll.removeFromPosition(4)
dll.printList()