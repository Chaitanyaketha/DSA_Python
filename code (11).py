def getsecmax(l):
    if len(l)<1:
        return None
    else:
        lar=l[0]
        slar=None
        for i in l:
            if lar>i:               #if current element is greater than lar(largest element)
                slar=lar            #update slar to largest
                lar=i               #update lar to current element(largest)
            elif(slar==None or slar<i):        #if x is less then largest and not equal to lar(largest element)
                slar=i                            #assign current element is second largest
    return slar
    
l=[10,32,34,1211,52,100]
print(getsecmax(l))