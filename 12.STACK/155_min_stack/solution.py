"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

"""
class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stackList = []
        self.min = float("inf")

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.min = min(self.min, x)
        self.stackList.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if len(self.stackList) != 0:
            top = self.stackList.pop(-1)
            if top == self.min and self.stackList:
                self.min = min(self.stackList)
            if not self.stackList:
                self.min = float("inf")
                
    def top(self):
        """
        :rtype: int
        """
        if len(self.stackList) != 0:
            return self.stackList[-1]
        
    def getMin(self):
        """
        :rtype: int
        """
        if self.stackList:
            return self.min

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()