#Prints all divisors but not necessarily in order
# def printdivisors(n):
#     i=1
#     while(i*i<=n):
#         if(n%i==0):
#             print(i)
#             if(i!=n//i!):
#                 print(n//i)
#         i=i+1
        
#Prints all divisors in Sorted Order       
def printDivisors(n):
    i=1 
    while(i*i<n):          #  for i in range(1, int(n**0.5) + 1):
        if(n%i==0):
            print(i)
        i=i+1
    while(i>=1):
        if(n%i==0):
            print(n//i)
        i=i-1
            
            
n=15
printDivisors(n)
# printDivisors2(n)