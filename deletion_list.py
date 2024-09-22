def delete_element(arr,pos):
    if pos<0 or pos>len(arr):
        print("invalid position ...")
        return
    else:
        delete_element=arr.pop(pos)
        print("deleted element = ",delete_element)
        print("array after deletion ... ",arr)
arr=[1,2,3,4,5,6]
print("original array ",arr)
pos=int(input("enter position ... "))
delete_element(arr,pos)
