class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        if len(prices) == 2:
            return prices[1] - prices[0] if prices[1] > prices[0] else 0
        
        low, high, sum, i = 0, 0, 0, 0
    
        while i < len(prices)-2:
            #keep incrementing i until we found a pair in which pre ele < next ele (slope going up)
            while prices[i] >= prices[i+1]:
                print(i)
                i+=1
                if i == len(prices)-1:
                    break
            #if the last ele is met, break the outer while loop 
            #which means the prices are decreasing all the way to the last element
            if i == len(prices)-1:
                break
            else:
                low, high = prices[i], prices[i+1]
                i+=1
                # if we reach to the last ele of list
                if i == len(prices)-1:
                    if prices[i] >= high:
                        high = prices[i]
                        sum += high-low
                        break
                else:  
                    while prices[i+1] >= prices[i]:
                        i+=1
                        if i == len(prices) -1:
                            break
                    high = prices[i]
                    sum += high - low
        return sum




#my solution is the not the best take a look at the leetcode third solution


