class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
class CircularLinkedList:
    def __init__(self):
        self.tail=None
        self.head=None
    def insert_head(self,value):
        new_node=Node(value)
        if self.tail==None:
            self.tail=new_node
            new_node.next=new_node
        else:
            new_node.next=self.tail.next
            self.tail.next=new_node
    def insert_last(self,value):
        new_node=Node(value)
        if self.tail==None:
            self.tail=new_node
            new_node.next=new_node
        else:
            new_node.next=self.tail.next
            self.tail.next=new_node
            self.tail=new_node
    def delete_all(self):
        self.tail=None
    def delete_first(self):
        if self.tail==None:
            print("List is empty")
            return
        if self.tail.next==self.tail:
            self.tail=None
        else:
            self.tail.next=self.tail.next.next
    def delete_last(self):
        if self.tail==None:
            print("List is empty")
            return
        if self.tail.next==self.tail:
            self.tail=None
            return
        curr=self.tail.next
        while curr.next!=self.tail:
            curr=curr.next  
        curr.next=self.tail.next
        self.tail=curr        
    def remove(self,value):
        if self.tail==None:
            print("Linked list is empty")
            return
        if self.tail.next.data==value:
            return self.delete_first()
        curr=self.tail.next
        while curr.next!=self.tail:
            if curr.next.data==value:
                break
            curr=curr.next  
        if curr.next==self.tail:
            print("Not found")   
        else:
            curr.next=curr.next.next
    def search(self,item):
        curr=self.tail.next
        pos=0
        while curr.next!=curr:
            if curr.data==item:
                print(pos)
                break
            curr=curr.next
            pos=pos+1 
        else:
            print("Element not found !")
    def traverse(self):
        if self.tail==None:
            print("Nothig to display....")
            return
        curr=self.tail.next
        while curr:
            print(curr.data,end=" ")
            curr=curr.next  
            if curr==self.tail.next:
                break
            print("->",end=" ")
if __name__=="__main__":
    linked_list=CircularLinkedList()

    while(True):
        print("\nMenu")
        print("1.Insert First")
        print("2.Insert Last")
        print("3.Insert After")
        print("4.Insert before")
        print("5.Delete all")
        print("6.Delete first")
        print("7.Delete last")
        print("8.Search element")
        print("9.Delete element By value")
        print("10.Display")
        print("11.Exit")

        choice=input("Enter Your choice : ")
        if choice=="1":
            data=input("Enter data to insert first : ")
            linked_list.insert_head(data)
        elif choice=="2":
            data=input("Enter data to insert Last : ")
            linked_list.insert_last(data)
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
            linked_list.delete_first()
        elif choice=="7":
            linked_list.delete_last()
        elif choice=="8":
            data=input("Enter the value that you want to search : ")
            linked_list.search(data)
        elif choice=="9":
            data=input("Enter the value that you want to delete : ")
            linked_list.remove(data)
        elif choice=="10":
            linked_list.traverse()
        elif choice=="11":
            print("Exiting program")
            break
        else:
            print("Invalid choice ....")