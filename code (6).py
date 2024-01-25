# Check for Prime
# naive

def prime(n):
    if n==1:
        return False
    else:
        i=2
        while(i*i<=n):  #or n>=i*i
            if n%i==0:
                return False
            i=i+1
        return True
    

n = 37
print(prime(n))

#There is another SUPER EFFICINET APPROACH AS WELL
def isprime(n) :
    if n == 1 :
        return False
        
    if n == 2 or n == 3 :
        return True
        
    if n % 2 == 0 or n % 3 == 0:
        return False
        
    i = 5
    while (i * i <= n) :
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
        
    return True