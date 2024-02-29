                       ### METHOD 1 USING RECURSION from 2nd node to end and later the 1st node ##########

class Node:
    def __init__(self, k):
        self.key = k
        self.next = None


def reverseList(head):
    if head == None:  #base cases os empty ll & only single node should be hadled explicitly else errors
        return head

    if head.next == None:
        return head

    rest_head=reverseList(head.next)       #our idea is to reverse the linked list from the 2nd node till the end and rest_head points towards the last node
    rest_tail=head.next                 #now create the rest_tail that points to the 2nd node of the LL ny simply assiging the head.next as it contains the head contains the address of the 2nd node only******
    rest_tail.next=head       #now think the linked list is almost revfersed so that the 1st node is now should br the last node and that can be acheived by doing the following code logic(visualize pictorially)
    head.next=None           #as head is the last node now then its next should be None
    return rest_head          #return the rest_head as it is the first node now 


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

head = reverseList(head)

printList(head)
