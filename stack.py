class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
class Stack:
    def __init__(self):
        self.top=None
    def push(self,value):
        new_node=Node(value)
        new_node.next=self.top
        self.top=new_node
    def pop(self):
        if self.top==None:
            print("Stack is empty")
            return
        self.top=self.top.next
    def peak(self):
        if self.top==None:
            print("Stack is empty")
        else:
            print(self.top.data)
    def traverse(self):
        if self.top==None:
            print("Stack is empty")
        curr=self.top
        while curr!=None:
            print(curr.data)
            curr=curr.next
if __name__=="__main__":
    obj=Stack()

    while(True):
        print("\nMenu")
        print("1.Push")
        print("2.Pop")
        print("3.Display")
        print("4.Peak")
        print("5.Exit")
        choice=input("Enter Your choice : ")
        if choice=="1":
            data=input("Enter data : ")
            obj.push(data)
        elif choice=="2":
            obj.pop()
        elif choice=="3":
            obj.traverse()
        elif choice=="4":
            obj.peak()
        elif choice=="5":
            print("Exiting program")
            break
        else:
            print("Invalid choice ....")