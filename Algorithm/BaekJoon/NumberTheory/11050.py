def factorial(n):
    if n<2:
        return 1
    
    else:
        return n*factorial(n-1)
    
    
n,k=map(int,input().split())

print(int(factorial(n)//factorial(k)//factorial(n-k)))