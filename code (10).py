def getMax(l):
    # if not l:
    #     return None  #if the list is empty
    # else:

    #     res = l[0]                  # assume l[0] is the max
    #     for i in range(1, len(l)):  # iterate through index 1 to last
    #         if l[i] > res:           # check whether current element is greater than res
    #             res = l[i]          # if current element is greater than res ,update res to current
    #     return res
    if not l:
        return None
    else:
        greatest=l[0]
        for i in range(1,len(l)):
            if (l[i] > greatest):
                greatest=l[i]
    return greatest
    

# O(n)

l = [int(x) for x in input().split()]
print(getMax(l))