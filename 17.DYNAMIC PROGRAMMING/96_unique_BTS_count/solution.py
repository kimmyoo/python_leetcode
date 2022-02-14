class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.helper(1, n)
    
    def helper(self, start, end):
        # when start > end, it points to the same node so there is only one possible structure
        if start > end:
            return 1
        
        total = 0
        for curVal in range(start, end+1):
            leftTotal = self.helper(start, curVal-1)
            rightTotal = self.helper(curVal+1, end)
            for i in range(leftTotal):
                for j in range(rightTotal):
                    total += 1
        return total
    """
    the recursive method exceeds time limit
    """

    def numTreesB(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Dynamic programming
        # 
        cache = [1] * (n+1)
        
        for numOfNodes in range(2, n+1):
            total = 0
            for rootOrder in range(1, numOfNodes+1):
                numOfLeftNodes = rootOrder - 1
                numOfRightNodes = numOfNodes - rootOrder
                total += cache[numOfLeftNodes] * cache[numOfRightNodes]
            cache[numOfNodes] = total
        
        return cache[n]