class Queue:
    def __init__(self,capacity):
        self.front=self.rear=-1
        self.capacity=capacity
        self.queue=[None]*capacity
    def enqueue(self,value):
        if self.isFull():
            print("Queue is full ... ")
            return
        elif self.isEmpty():
            self.front=self.rear=0
        else:
            self.rear=(self.rear+1)% self.capacity
        self.queue[self.rear]=value
    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty can not delete ...")
            return
        if self.front==self.rear:
            temp=self.queue[self.front]
            self.front=self.rear=-1
            return temp
        else:
            temp=self.queue[self.front]
            self.front=(self.front+1) % self.capacity
            print("deleted item = ",temp)
            return temp
    def isFull(self):
        return (self.rear+1)%self.capacity==self.front
    def isEmpty(self):
        return self.front==-1
    def traverse(self):
        if self.isEmpty():
            print("Queue is empty nothing to display ... ")
            return
        i=self.front
        while True:
            print(self.queue[i])
            if i==self.rear:
                break
            i=(i+1)%self.capacity
obj=Queue(3)
obj.enqueue(10)
obj.enqueue(20)
obj.enqueue(30)
obj.dequeue()
obj.enqueue(40)
obj.traverse()