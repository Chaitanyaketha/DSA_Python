class Node:
    def __init__(self, k):
        self.key = k
        self.next = None


def insertPos(head,data,pos):

    temp = Node(data)

    if pos ==1:                    #It means that there are no nodes previously.so the new node will be the 1st in LL
        temp.next = head
        return temp             #simply return the LL to print it
    curr = head

    for i in range(pos-2):        # POS-2 is the logical position to set the node at any position 
        curr = curr.next 
        if curr == None:           #If the pos provided is out of pos of LL
            return head            # then simply return the LL

    temp.next = curr.next         #Here be pay attention to form the link between the nodes because the vice versa of these two lines of codes will make the code incorrect 
    curr.next = temp               #follow the link establishment of nodes carefully

    return head        #so finally return the head to print and traverse till the end


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
head.next.next.next.next = Node(50)

printList(head)

head = insertPos(head,45,4)

printList(head)
