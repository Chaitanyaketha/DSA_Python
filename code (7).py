def isprime(X):
    if X==1:
        return False
    else:
        p=2
        while(p*p<=X):  #for i in range(2,(X**0.5)+1)********** for the square root decreased interations
            if(X%p==0):
                return False
            p=p+1
        return True
        
def PrimeFactors(n):
    for i in range(2,n+1):
        if isprime(i):
            x = i
            while(n%x==0):
                print(i)
                x=x*i
                

n = int(input("Enter n:\n"))
PrimeFactors(n)