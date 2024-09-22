a=[10,12,14,16,18,20]
l=len(a)
f=0
beg=0
end=l-1
x=int(input("Enter a number for searching "))
while beg<=end:
    mid=(beg+end)//2
    if a[mid]==x:
        print("Element found at position ... ",mid+1)
        f=f+1
        break
    elif a[mid]>x:
        end=mid-1
    else:
        beg=mid+1
if f==0:
    print("element not found")