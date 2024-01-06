from collections import deque

"""
implemented using two stacks(lists, this case)
when pushing, push it to inStack
when popping or peeking, move all elements to outStack

"""
class MyQueue:

    def __init__(self):
        self.inStack = []
        self.outStack = []

    def push(self, x: int) -> None:
        self.inStack.append(x)

    def pop(self) -> int:
        self.inToOut()
        return self.outStack.pop()

    def peek(self) -> int:
        self.inToOut()
        return self.outStack[-1] # the top element of outStack

    def empty(self) -> bool:
        return len(self.inStack) == 0 and len(self.outStack) == 0
    
    # inToOut moves all elements to from inStack to outStack
    def inToOut(self):
        if len(self.outStack) == 0:
            while len(self.inStack):
                self.outStack.append(self.inStack.pop())




from collections import deque
"""
implemented using deque(), the pop was handled by popleft() method of deque
for deque, append(), appendleft(), pop(), and popleft() all have a time complexity of O(1),
making them extremely efficient.
"""
class MyQueueVer2:

    def __init__(self):
        self.stack = deque()

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.popleft()

    def peek(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return len(self.stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()