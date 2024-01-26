def rotateByone(l):
    # n = len(l)
    # x = l[0]
    # for i in range(1, n):
    #     l[i - 1] = l[i]

    # l[n - 1] = x
    p=l[0]
    for i in range(1,len(l)):
        l[i-1]=l[i]
        
    l[-1]=p
    
    
    ###################################################
l.append(pop(l[0]))
print(l)

l = [10, 20, 30, 40]
rotateByone(l)
print(l)
