def swap1(a,b):
    a = a + b
    b = a - b
    a = a - b
    return a,b
def swap2(a,b):
    a=a^b
    b=a^b
    a=a^b
    return a,b
def swap3(a,b):
    a,b = b,a
    return a,b

if __name__=="__main__":
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))
    print(f"the before swapping a={a} and b={b}")
    a,b=swap1(a,b)
    print(f"the after 1 swapping a={a} and b={b}")
    a,b=swap2(a,b)
    print(f"the after 2 swap a={a} and b={b}")
    a,b=swap3(a,b)
    print(f"the after 3 swap a={a} and b={b}")
