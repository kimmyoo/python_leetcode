class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0 
        match = {'(':')', '{':'}', '[':']'}
        stack = []

        while ( i <= len(s)-1):
            if s[i] in match:
                stack.append(s[i])
            else:
                if (stack):
                    topOfStack = stack.pop()
                    print(topOfStack, s[i])
                    if match[topOfStack] != s[i]:
                        return False
                else:
                    return False
            i+=1
        if len(stack) > 0:
            return False
        return True 
        
s = Solution()

res = s.isValid("(){}{{{}}}{{{{{((((()))))}}}}}")
print(res)