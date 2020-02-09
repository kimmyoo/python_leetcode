class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.backtrack("", 0, 0, n, res)
        return res
    
    #backtracking is always recursive but there will be an ending
    #condition to terminate the recursive call. The trick is to find the ending condition
    def backtrack(self, st, left, right, l, ans):
        if len(st) == 2*l:
            ans.append(st)
            return
        if left < l:
            self.backtrack(st+"(", left+1, right, l, ans)
        if right < left:
            self.backtrack(st+")", left, right+1, l, ans)


s = Solution()
res = s.generateParenthesis(3)
print(res)