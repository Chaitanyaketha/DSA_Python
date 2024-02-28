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


    
def removeDups(head):
    curr = head
    while curr!= None and curr.next!= None:       # consider these checks to avoid the errors in corner cases,ex when only one node is present
        if curr.data == curr.next.data :           #then there wont be any curr.next.data in case of single node LL
            curr.next = curr.next.next
        else:
            curr= curr.next                       #if the next node not is not duplicate then only we move CURR to the next node
            
    
    
    
        

head = Node(10)
head.next = Node(10)
head.next.next = Node(20)


printList(head)
removeDups(head)
printList(head)
