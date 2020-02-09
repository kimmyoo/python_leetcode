"""
Implement the following operations of a stack using queues.
push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
"""
import collections

class Stack:
    def __init__(self):
        self.queue = collections.deque()
    # original: a - b - c
    # push z:  a - b - c -z 
    #          b - c - z - a
    #          c -z - a - b
    #          z - a - b - c 
    def push(self, x):
        q = self.queue
        q.append(x)
        for _ in range(len(q) - 1):
            q.append(q.popleft())
        
    def pop(self):
        return self.queue.popleft()

    def top(self):
        return self.queue[0]
    
    def empty(self):
        return not len(self.queue)

stack = Stack()
stack.push(1)
stack.push(2)
print(stack.top())
print(stack.pop())
print(stack.empty())