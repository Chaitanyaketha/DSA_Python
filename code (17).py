def binconverter(n):
    if n==0:
        return 
    binconverter(n//2)
    print(n%2)
binconver(13)