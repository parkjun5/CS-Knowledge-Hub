from collections import deque

stack = []

stack.append(1)
stack.append(5)
stack.append(2)
stack.append(7)
stack.append(123)

stack.pop()

print(stack)
print(stack[::-1])


queue = deque()

queue.append(3)
queue.append(6)
queue.append(32)
queue.append(-1)

queue.popleft()

print(queue)
queue.reverse()
print(queue)

