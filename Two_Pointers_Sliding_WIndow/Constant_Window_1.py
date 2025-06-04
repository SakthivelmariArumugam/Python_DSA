#the below program me using constant window method in the program
#the program input list1=[1,3,4,2,4,6,9,8,2] and k=4
#the output is find the continuous k number values to find the max sum in array
def max_sum(list1,k):
  sum=1
  l=0
  r=k-1
  for i in range(l,r+1):
    sum=sum+list1[i]
  max_sum=sum
  while(r<len(list1)-1):
    sum=sum-list1[l]
    l=l+1
    r=r+1
    sum=sum+list1[r]
    max_sum=max(max_sum,sum)
  return max_sum



value=max_sum([1,3,4,2,4,6,9,8,2],4)
print(value)
