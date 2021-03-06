class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        refer to 78: subsets no duplicates
        """
        res = []

        def dfs(k, startIndex, curr):
            if len(curr) == k:
                res.append(curr[:])
                return
            for i in range(startIndex, n):
                curr.append(i+1)
                dfs(k, i+1, curr)
                curr.pop()
        dfs(k, 0, [])
        return res