class Node:
    def __init__(self,value):
        self.prev=None
        self.data=value
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insert_head(self,value):
        new_node=Node(value)
        if self.head==None:
             self.head=new_node  
        else:
             self.head.prev=new_node
             new_node.next=self.head
             self.head=new_node  
    def append(self,value):
        new_node=Node(value)
        if self.head==None:
            self.head=new_node 
            return
        curr=self.head
        while curr.next!=None:
            curr=curr.next
        curr.next=new_node
        new_node.prev=curr
    def insert_after(self,after,value):
        new_node=Node(value)
        if self.head==None:
            print("Linked list is empty")
            return
        curr=self.head
        while curr!=None:
            if curr.data==after:
                break
            curr=curr.next 
        if curr!=None:
            new_node.prev=curr
            new_node.next=curr.next
            if curr.next is not None:
                curr.next.prev=new_node
            curr.next=new_node
        else:
            print("Element not found")
    
    def insert_before(self,before,value):
        new_node=Node(value)
        curr=self.head
        while curr!=None:
            if curr.data==before:
                break
            curr=curr.next
        if curr!=None:
            new_node.next=curr
            new_node.prev=curr.prev
            if curr.prev==None:
                self.head=new_node
            if curr.prev is not None:
                curr.prev.next=new_node
            curr.prev=new_node
            
        else:
            print("Element not found")
    def delete_all(self):
        self.head=None
    def delete_head(self):
        if self.head==None:
            print("Linked list is empty")
            return
        self.head=self.head.next
    def pop(self):
        if self.head==None:
            print("empty linked list")
            return
        curr=self.head
        if curr.next==None:
            return self.delete_all()
        while curr.next.next!=None:
            curr=curr.next
        curr.next=None
    def remove(self,item):
        if self.head==None:
            print("Linked list is empty ")
            return
        curr=self.head
        if curr.data==item:
            return self.delete_head()
        while curr!=None:
            if curr.data==item:
                break
            curr=curr.next
        if curr!=None:
            curr.prev.next=curr.next
            if curr.next is not None:
                curr.next.prev=curr.prev
        else:
            print("Element not found")
    def search(self,item):
        curr=self.head
        pos=0
        while curr!=None:
            if curr.data==item:
                print(pos)
                break
            curr=curr.next
            pos=pos+1
        else:
            print("Element not found !")
    def traverse(self):
        if self.head==None:
            print("Linked list is empty")
            return
        curr=self.head
        while curr!=None:
            print(curr.data,end="->")
            curr=curr.next
if __name__=="__main__":
    linked_list=LinkedList()


    while(True):
        print("\nMenu")
        print("1.Insert First")
        print("2.Insert Last")
        print("3.insert after")
        print("4.insert before")
        print("5.Delete all")
        print("6.Delete first")
        print("7.Delete last")
        print("8.Remove by value")
        print("9.Search by value ")
        print("10.Display")
        print("11.Exit")


        choice=input("Enter Your choice : ")
        if choice=="1":
            data=input("Enter data to insert first : ")
            linked_list.insert_head(data)
        elif choice=="2":
            data=input("Enter data to insert last: ")
            linked_list.append(data)
        elif choice=="3":
            data=input("Enter data to insert : ")
            item=input("Enter the item after you want insert data : ")
            linked_list.insert_after(item,data)
        elif choice=="4":
            data=input("Enter data to insert : ")
            item=input("Enter the item before you want insert data : ")
            linked_list.insert_before(item,data)
        elif choice=="5":
            linked_list.delete_all()
        elif choice=="6":
            linked_list.delete_head()
        elif choice=="7":
            linked_list.pop()
        elif choice=="8":
            item=input("Enter item That you want to delete: ")
            linked_list.remove(item)
        elif choice=="9":
            data=input("Enter data to find  ")
            linked_list.search(data)
        elif choice=="10":
            linked_list.traverse()
        elif choice=="11":
            print("Exiting program")
            break
        else:
            print("Invalid choice ....")