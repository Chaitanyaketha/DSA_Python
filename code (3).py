#efficient method
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
n=int(input())
print(factorial(n))

#unoptimized way
def factorial(n):
    if n==0 or n==1:
        return n
    else:
        fact=1
        while(n>1):
            fact=fact*n
            n=n-1
    return fact
n=int(input())
print(factorial(n))