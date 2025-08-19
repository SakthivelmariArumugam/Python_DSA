list1=[13,46,24,52,20,9]
for i in range(len(list1)-1):
    r=i
    small=list1[i]
    for j in range(i,len(list1)):
        if list1[j]<list1[r]:
            r=j 
    list1[r],list1[i]=list1[i],list1[r]
print(list1)
#Time Complexity of the Selection Sort Algorithm
# n+(n-1)+(n-2)+(n-3)(n-n-1)=n(n+1)/2=n/2+n2/2
#ignore smaller value so n2/2
#so Time complexity of the selection sort is O(n2)
    