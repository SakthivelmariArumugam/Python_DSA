def is_even(a):
  if(a%2==0):
    return True
  else:
    return False
  
def is_even2(n):
  if n&1==0:
    return True
  else:
    return False

if __name__=="__main__":
  n=int(input("Enter the number:"))
  if is_even(n) or is_even2(n):
    print(f"the number {n} is even")
  else:
    print(f"the number {n} is odd")
