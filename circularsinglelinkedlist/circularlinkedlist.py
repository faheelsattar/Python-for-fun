class Node:
    def __init__(self,value:int):
        self.value=value
        self.next=None

class CircularLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.counter=0
    
    def insertAtBegninning(self,value:int):
        node = Node(value)
        if self.head is None:
            node.next=self.head
            node.next=node
            self.head=node
            self.tail=node
        else:
            tempnode = self.head
            while (tempnode.next != self.head):
                tempnode=tempnode.next
            tempnode.next=node
            node.next=self.head
            self.head=node
        self.counter+=1

    def insertAtEnd(self,value:int):
        node= Node(value)
        if self.head == None:
            self.head= node
            self.tail= node
        else:
            tempnode= self.head
            while (tempnode.next):
                tempnode=tempnode.next
            tempnode.next=node
            node.next=self.head
            self.tail=node
        self.counter+=1

    def insertAtPosition(self, value:int, position:int):
        if position == 1:
            self.insertAtBegninning(value)
        else:
            i=0 
            node= Node(value)
            prevnode=self.head
            nextnode=self.head
            while (i!=position-1):
                prevnode=nextnode
                nextnode=nextnode.next
                i+=1
            node.next=nextnode
            prevnode.next=node
            self.counter+=1

    def removeFromBeginning(self):
        tempnode = self.head
        self.head=tempnode.next
        self.tail.next= self.head
        tempnode=None
        self.counter-=1

    def removeFromEnd(self):
        prevnode= self.head
        nextnode = self.head
        while (nextnode.next != self.head):
            prevnode=nextnode
            nextnode=nextnode.next
        prevnode.next=nextnode.next
        self.tail=prevnode
        nextnode=None  
        self.counter-=1

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
            nextnode=None  
            self.counter-=1
        
    def printLinkedList(self):
        tempnode=self.head
        while (True):
            print(tempnode.value)
            tempnode= tempnode.next
            if tempnode == self.head:
                break

l1= CircularLinkedList()
l1.insertAtBegninning(2)
l1.insertAtBegninning(1)
l1.insertAtBegninning(0)
l1.insertAtBegninning(12)
l1.insertAtPosition(41,1)
l1.removeFromBeginning()
l1.removeFromPosition(4)
l1.printLinkedList()
