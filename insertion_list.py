def insert_element(arr,element,position):
    if position<0 or position>len(arr):
        print("Invalid position ... ")
        return
    if position==0:
        return [element]+arr
    elif position>=len(arr):
        return arr+[element]
    else:
        return arr[:position]+[element]+arr[position:]
arr=[1,2,3,4,5,6,7]
print("original array is ", arr)
element=int(input("enter a element ... "))
position=int(input("Enter position .."))
arr1=insert_element(arr,element,position)
print(arr1)
