a=[10,11,12,13,9,8,75]
l=len(a)
f=0
x=int(input("Enter a number for searching : "))
for i in range(l):
    if a[i]==x:
        print("Your element at position ",i+1)
        f+=1
        break
if f==0:
    print("Element not found")