class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
    def enqueue(self,value):
        new_node=Node(value)
        if self.rear==None:
            self.front=new_node
            self.rear=self.front
        else:
            self.rear.next=new_node
            self.rear=new_node
    def dequeue(self):
        if self.front==None:
            print("empty linked list")
            return
        self.front=self.front.next
    def traverse(self):
        if self.front==None:
            print("Queue is empty")
        curr=self.front
        while curr!=None:
            print(curr.data)
            curr=curr.next
if __name__=="__main__":
    obj=Queue()

    while(True):
        print("\nMenu")
        print("1.enqueue")
        print("2.dequeue")
        print("3.Display")
        print("4.Exit")
        choice=input("Enter Your choice : ")
        if choice=="1":
            data=input("Enter data : ")
            obj.enqueue(data)
        elif choice=="2":
            obj.dequeue()
        elif choice=="3":
            obj.traverse()
        elif choice=="4":
            print("Exiting program")
            break
        else:
            print("Invalid choice ....")