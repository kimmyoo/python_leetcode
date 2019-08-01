class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #maintain two variables: currMin and maxProf
        if len(prices) == 0:
            return 0
        currMin = max(prices)
        maxProf = 0
        for i in range (0, len(prices)):
            if prices[i] < currMin:
                currMin = prices[i]
                #print(currMin)
            elif prices[i] - currMin > maxProf:
                maxProf = prices[i] - currMin
        return maxProf

#test code
s = Solution()
prices1 = [7,1,5,3,6,4]
prices2 = [5, 4, 3, 2, 1]
prices3 = [3,3,3,3]

res1 = s.maxProfit(prices1)
res2 = s.maxProfit(prices2)
res3 = s.maxProfit(prices3)
print(res1, res2, res3)