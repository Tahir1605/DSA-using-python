a=[32,12,16,14,2,8]
print("Before sorting : ",a)
l=len(a)
for i in range(l):
    j=i
    while(j>0):
        if(a[j-1]>a[j]):
            temp=a[j]
            a[j]=a[j-1]
            a[j-1]=temp
        j-=1
print("After sorting : ",a)
