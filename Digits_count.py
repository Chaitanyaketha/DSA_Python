x = int(input("Enter x:\n"))

c = 0

while x>0:
    
    x=x//10
    c = c + 1
    
print("count of digit is :",c)
