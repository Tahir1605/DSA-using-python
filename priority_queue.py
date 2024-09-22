class PriorityQueue:
    def __init__(self,capacity):
        self.capacity=capacity
        self.queue=[]
    def isEmpty(self):
        return len(self.queue) == 0
    def enqueue(self,item,priority):
        if len(self.queue)==self.capacity:
            print("Queue is full ")
            return
        self.queue.append((item,priority))
        self.queue.sort(key=lambda x : x[1])
    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty ")
            return None
        return self.queue.pop(0)[0]
    def display(self):
        if self.isEmpty():
            print("Queue is empty ")
            return
        print("Priority queue :")
        for item,priority in self.queue:
            print(f"item:{item},Priority:{priority}")
obj=PriorityQueue(5)
obj.enqueue(10,5)
obj.enqueue(20,4) 
obj.enqueue(60,3)
obj.enqueue(30,2)
obj.enqueue(40,10)
obj.dequeue()
obj.display()

