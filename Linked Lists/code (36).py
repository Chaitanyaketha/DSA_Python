class Node:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def reverseDll(head):
    if head == None:
        return None
    if head.next == None:         #two base cases
        return head

    curr = head
    prev = None     ###

    while curr != None:
        prev = curr              ###### HERE WE ARE STORING PREV BECAUSE THE LAST PREV IS GOING TO BE HEAD AFTER THE COMPLETE PROCESS
        curr.next, curr.prev = curr.prev, curr.next       ##swapping to make DLL reversed
        curr = curr.prev          #Note how the pointer moves to the next node @@PREV

    return prev    


def printDll(head):
    curr = head
    while curr != None:
        print(curr.data, end=" ")
        curr = curr.next
    print()


head = Node(10)
temp1 = Node(20)
temp2 = Node(30)

head.next = temp1
temp1.prev = head

temp1.next = temp2
temp2.prev = temp1

printDll(head)

head = reverseDll(head)

printDll(head)
