class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        #totalLeft is used to see if we have used up all gas
        gasLeft, startIndex, totalLeft = 0, 0, 0
        
        for i in range(len(gas)):
            gasLeft += gas[i] - cost[i]
            totalLeft += gas[i] - cost[i]
            
            if gasLeft < 0:
                startIndex = i + 1
                gasLeft = 0
        if totalLeft < 0:
            return -1
        return startIndex