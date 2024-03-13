from _collections import deque

q = deque()

q.append(10)
q.append(20)
q.append(30)
print(q)
print(q.popleft())
q.append(40)
print(q.popleft())
print(len(q))
print(q[0])
print(q[-1])



################  USING THE LIST ALSO QUEUE CAN BE IMPLEMENTED BUT NOT SUGESSTED AS TIME COMPLEXITY CONSIDERATIONS

q = []
q.append(10)
q.append(20)
q.append(30)

print(q)
print(q.pop(0))
print(q)
q.append(40)
print(q)
print(q.pop(0))
print(q)
print(len(q))
print(q[0])
print(q[-1])
