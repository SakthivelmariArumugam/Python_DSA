
def Multiplication_Table(n):
  for i in range(1,17):
    num=i*n
    print(f"{i}*{n}={num}")

if __name__=="__main__":
  n=int(input("Enter the number:"))
  Multiplication_Table(n)
