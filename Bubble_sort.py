a=[32,12,16,14,2,8]
print("Before sort : ",a)
l=len(a)
for i in range(l):
    for j in range(l-i-1):
        if(a[j]>a[j+1]):
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
print("After sort : ",a)
