class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        if not mat:
            return []
        
        res = []
        row = len(mat)
        power = []
        
        for i in range(row):
            power.append((sum(mat[i]), i))
        
        # sorting a list of tuple 深学习一下
        power.sort()

        for i in range(k):
            res.append(power[i][1])
        return res
