from collections import deque
 
class Solution:
    def maxDepth(self, s: str) -> int:
        stack = deque()
        mx = 0
        for ch in s:
            if ch == '(':
                stack.append('(')
            # only when seeing a ')' update mx
            # then remove counter part in stack
            if ch == ')':
                mx = max(mx, len(stack))
                stack.pop()
        return mx

    # or maybe simply a counter
    def maxDepth2(self, s: str) -> int:
        counter = 0
        mx = 0
        for ch in s:
            if ch == '(':
                counter+=1
            if ch == ')':
                counter-=1
            mx = max(mx, counter)
        return mx