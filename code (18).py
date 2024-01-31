#printing the numbers from 1 to n 
# def print1toN(n):
#     if(n==0):
#         return
#     print1toN(n-1)
#     print(n)
    
# print1toN(3)

#printing the numbers from n to 1 
def printNto1(n):
    if n==0:
        return
    print(n)
    printNto1(n-1)
    
printNto1(3)