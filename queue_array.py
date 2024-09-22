class Queue:
    def __init__(self,capacity):
        self.front=-1
        self.rear=-1
        self.capacity=capacity
        self.queue=[None]*capacity
    def enqueue(self,value):
        if self.rear==self.capacity-1:
            print("Queue is full ... ")
            return
        if self.front==-1:
            self.front+=1
        self.rear+=1
        self.queue[self.rear]=value
    def dequeue(self):
        if self.rear==-1:
            print("Queue is empty can not delete ...")
            return
        if self.front==self.rear:
            temp=self.queue[self.front]
            self.front=self.rear=-1
            return temp
        else:
            temp=self.queue[self.front]
            self.front+=1
            print("deleted item = ",temp)
            return temp
    def peak(self):
        if self.rear==-1:
            print("Queue is empty ... ")
            return
        print("Top most element in the Queue is ",self.queue[self.rear])
    def isFull(self):
        if self.rear==self.capacity-1:
            print("Queue is full  ... ")
        else:
            print("Queue is not full ... ")
    def isEmpty(self):
        if self.rear==-1:
            print("Queue is empty ... ")
        else:
            print("Queue is not empty ... ")
    def traverse(self):
        if self.rear==-1:
            print("Queue is empty nothing to display ... ")
            return
        i=self.rear
        while i>=self.front:
            print(self.queue[i])
            i-=1
obj=Queue(3)
obj.enqueue(10)
obj.enqueue(20)
obj.enqueue(30)
obj.dequeue()
obj.traverse()
