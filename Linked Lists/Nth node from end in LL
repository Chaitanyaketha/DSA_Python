        ####    NTH NODE FROMM THE END OF THE LL   #####


class Node:
    def __init__(self, k):
        self.data = k
        self.next = None

def printList(head):
    curr = head
    while curr != None:
        print(curr.data, end=" ")
        curr = curr.next
    print()


    
def printNthFromEnd(head,n):
    len = 0 
    curr = head
    while curr:   #for finding the len of LL
        curr=curr.next
        len+=1
    if len<n :        # Case where index is out of range
        return
    curr = head 
    for i in range (1,len-n+1):   #Iterate till we reach the len-n+1 pos to get the element 
        curr = curr.next
    print(curr.data)
        
    
            
head = Node(10)
head.next = Node(10)
head.next.next = Node(20)


printList(head)
printNthFromEnd(head,1)




                       ############    TWO POINTER/RREFERENCES Approach  #########

class Node:
    def __init__(self, k):
        self.data = k
        self.next = None

def printList(head):
    curr = head
    while curr != None:
        print(curr.data, end=" ")
        curr = curr.next
    print()


    
def printNthFromEnd(head,n):
    if head == None :
        return
    first = head                    
    for i in range (n):   ###For reaching the nth position from start
        if first == None:
            return
        first=first.next
    second=head
    while first!= None:           
        second=second.next    #refer notes
        first=first.next
    print(second.data)
        
        
    
            
head = Node(10)
head.next = Node(10)
head.next.next = Node(20)


printList(head)
printNthFromEnd(head,1)



