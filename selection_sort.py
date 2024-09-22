a=[32,24,26,8,9,15]
print("Before sorting : ",a)
l=len(a)
for i in range(l-1):
    m=i
    for j in range(i,l):
        if(a[m]>a[j]):
            m=j
    if(a[m]!=i):
        temp=a[i]
        a[i]=a[m]
        a[m]=temp
print("After sorting : ",a)
