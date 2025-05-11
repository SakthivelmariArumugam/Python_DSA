def sum(n):
  if(n%2==0):
    return(int) (n/2)*(n+1)
  else:
    return(int)((n+1)/2)*n

if __name__=="__main__":
  n=int(input("Enter the number:"))
  print(f"the sum of natural numbers:{sum(n)}")
