#fibonacci value

def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)
n=int(input())
print(fib(n))

#fibonacci with memoization dynamic programming (top down approach)

def fib(n,values):
    if n<=1:
        values[n]=n
    
    if values[n] is None:
        values[n]=fib(n-1,values)+fib(n-2,values)
    
    return values[n]

def main():
    n=int(input())
    values=[None]*100
    print("The Fibonacci value:",fib(n,values))

if __name__=="__main__":
    main()
    

#fibonacci with tabulation dynamic programming (bottom up approach)

def fib(n):
    result=[0]*100
    result[1]=1
    for i in range(2,n+1):
        result[i]=result[i-1]+result[i-2]
    
    return result[n]

def main():
    n=int(input())
    print("The Fibonacci value:",fib(n))

if __name__=="__main__":
    main()
    

