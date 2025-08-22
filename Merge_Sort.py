list1=[7,13,12,11,22]
def merge(arr,low,mid,high):
     r=arr[low:mid+1]
     l=arr[mid+1:high+1]
     i=0
     j=0
     k=low
     while i<len(r) and j<len(l):
         if r[i]<l[j]:
             arr[k]=r[i]
             i=i+1
             k=k+1
         else:
             arr[k]=l[j]
             j=j+1
             k=k+1
     while i<len(r):
         arr[k]=r[i]
         i=i+1
         k=k+1
     while j<len(l):
         arr[k]=l[j]
         j=j+1
         k=k+1
     return

def mergesort(arr,low,high):
    if low>=high:
        return
    mid=(low+high)//2
    mergesort(arr,low,mid)
    mergesort(arr,mid+1,high)
    merge(arr,low,mid,high)
mergesort(list1,0,len(list1)-1)
print(list1)