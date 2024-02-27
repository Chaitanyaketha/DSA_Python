class Node:
    def __init__(self, k):
        self.key = k
        self.next = None


def delFirst(head):
    if head == None:    #In the cases where no nodes are present or only one node is present
        return None
    else:
        return head.next   #simpley make the 1st node's next as the head so that 2nd node's value becomes the head.No need to worry about the 1st node because auto memory mangement in python


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

head = delFirst(head)

printList(head)
