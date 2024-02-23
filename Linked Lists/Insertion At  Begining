class Node:
    def __init__(self,key):
        self.key=key
        self.next=None

def insertBegin(head,key):
        temp=Node(key)      #creating a node and then assigning them to the before the head
        temp.next=head 
        return temp


head=None              #intially empty node 
head=insertBegin(head,10)    #creating a node and then assining back to the  head 
head=insertBegin(head,20)
head=insertBegin(head,30)

def printList(head):
    curr = head
    while curr!= None:
        print(curr.key, sep="->")
        curr = curr.next


printList(head)
