from collections import deque


d=[1,2,3,4,5,6,7,8,9,10]
q=deque(d)
print(q)

q.append(11)
print(q)

q.appendleft(12)
print(q)

q.pop()
print(q)

q.popleft()
print(q)

q.extend([13,14,15,16])
print(q)

q.extendleft([17,18,19,20])
print(q)

q.rotate(3)
print(q)
