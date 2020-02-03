
class Stack:
    
    def __init__(self, length:int):
        self.array =[None]*length
        self.top=-1

    def isFull(self):
        if len(self.array)-1 == self.top:
            return True
        else:
            return False

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def push(self, value:int):
        if self.isFull():
            return False
        else:
            self.top+=1
            self.array[self.top]=value
            return True

    def pop(self):
        if self.isEmpty():
            return False
        else:
           val= self.array[self.top]
           self.top-=1
           return val


    def peek(self):
        return self.top

    def deleteStack(self):
        self.array:None
    

stack =Stack(4)

print(stack.push(1))
print(stack.push(2))
print(stack.push(3))
print(stack.pop())
print(stack.push(4))
print(stack.pop())
print(stack.pop())
print(stack.pop())





