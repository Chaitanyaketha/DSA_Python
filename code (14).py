# def removeDuplicates(arr, n):
#     res=1 
#     for i in range(1, n):
#         if(arr[res-1]!=arr[i]):
#             arr[res]=arr[i]
#             res+=1
#     return res

def removeDuplicates(arr,n):
    temp=1
    for i in range(1,n):
        if(arr[temp-1]!=arr[i]):
            arr[temp]=arr[i]
            temp=temp+1
    return 3
            
    
    
n=7
arr=[10, 20, 20, 30, 30, 30, 30]
print(removeDuplicates(arr, n))