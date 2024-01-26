def isSorted(l):
    i = 1
     #USING WHILE LOOP
    while i< len(l):
         
        if l[i]<l[i-1]:
             
            return False
        i=i+1
        
    return True
    
l = [10,20,30,15,40]

if isSorted(l):
    print("Yes")
else:
    print("No")
    #####################################################################3
    #USING FOR LOOP
    
def sort1(l):
    for i in range(1,len(l)):
            if (l[i]<l[i-1]):
                return False
            
            
    return True
    
    
l=[10,20,20,30,60,100]
print(sort1(l))
         
         
         
         
         
         #####################
         def isSorted(l):
    l2 = sorted(l)          # note the DIFFERENCE BETWEEN SORTED() AND SORT() BOTH ARE NOT SAME
    
    if l==l2:
        return True
    else:
        return False

    
l = [10,20,30,15,40]

if isSorted(l):
    print("Yes")
else:
    print("No")
            