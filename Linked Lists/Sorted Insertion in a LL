class Node:
    def __init__(self, k):
        self.key = k
        self.next = None


def sortedInsert(head, x):
    temp = Node(x)

    if head == None:     #if no nodes are present 
        return temp
    elif x < head.key: #if the new node is less than the head 
        temp.next = head
        return temp
    else:
        curr = head     #general cases

        while curr.next != None and curr.next.key < x:
            curr = curr.next

        temp.next = curr.next
        curr.next = temp
        return head


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

h = head
while h != None:
    print(h.key)
    h = h.next

print()

h = sortedInsert(head, 35)

h = head
while h != None:
    print(h.key)
    h = h.next
