class Solution(object):
    def getHappyString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        allstrs = []
        charList = ["a", "b", "c"]

        def backtracking(curr):
            if len(curr) == n:
                allstrs.append(curr[:])
                return
            for ch in charList:
                #need to check if curr otherwise index will be out of range
                if curr and ch == curr[-1]:
                    continue
                curr = curr + ch
                backtracking(curr)
                curr = curr[:-1]

        backtracking("")
        if len(allstrs) < k:
            return ""
        #no need to sort()
        return allstrs[k-1]