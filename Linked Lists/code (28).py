class Node:
    def __init__(self, k):
        self.key = k
        self.next = None

def deleteNode(head):
    if head == None:
        return  None    #when no node is present 

    if head.next == None:  #if only one node is present
        return None

    curr = head

    while curr.next.next != None:      #To fond the 2nd LAST NODE**8
        curr = curr.next

    curr.next = None   #unlinking the lasst node 
    return head     #and retrun tyhe head for printing th LL



def printList(head):
    curr = head
    while curr != None:
        print(curr.key, end=" ")
        curr = curr.next
    print()


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

printList(head)

head = deleteNode(head)

printList(head)
