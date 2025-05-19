 
def Majority_Element(a):
  l=dict()
  for i in a:
    if i in l:
      l[i]=l[i]+1
    else:
      l[i]=1
  big=0
  value=l[a[0]]
  for i in a:
    if l[i]>big:
      value=i
      big=l[i]
  if big>int(len(a)/2):
    return value

print("the value:",Majority_Element([2,1,2,3,3,3,3]))
