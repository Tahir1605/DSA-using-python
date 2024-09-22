class Stack:
    def __init__(self,capacity):
        self.top=-1
        self.capacity=capacity
        self.stack=[None]*capacity
    def push(self,value):
        if self.top==self.capacity-1:
            print("Stack is full ...")
            return
        self.top+=1
        self.stack[self.top]=value
    def pop(self):
        if self.top==-1:
            print("Stack is empty can not delete ...")
            return
        temp=self.stack[self.top]
        self.top-=1
        print("deleted item = ",temp)
        return temp
    def peak(self):
        if self.top==-1:
            print("Stack is empty ... ")
            return
        print("Top most element in the stack is ",self.stack[self.top])
    def isFull(self):
        if self.top==self.capacity-1:
            print("Stack is full  ... ")
        else:
            print("Stack is not full ... ")
    def isEmpty(self):
        if self.top==-1:
            print("Stack is empty ... ")
        else:
            print("Stack is not empty ... ")
    def traverse(self):
        if self.top==-1:
            print("Stack is empty nothing to display ... ")
            return
        i=self.top
        while i>=0:
            print(self.stack[i])
            i-=1
obj=Stack(10)
obj.push(10)
obj.push(20)
obj.push(30)
obj.peak()
obj.pop()
obj.traverse()
