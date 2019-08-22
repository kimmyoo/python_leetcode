"""
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).
Once you pay the cost, you can either climb one or two steps. 
You need to find minimum cost to reach the top of the floor, 
and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6

Good explanation of DP on youtube
https://www.youtube.com/watch?v=Jakbj4vaIbE
"""
import numpy as np

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        l = len(cost)
        opt = np.zeros(l)
        # 0 means the cost coming from previous step
        opt[0], opt[1] = (0+cost[0]), (0+cost[1])
        #definition of opt is the min cost of leaving ith step either coming from (i-1)th step
        #or from (i-2)th step
        for i in range(2, l):
            opt[i] = min(opt[i-1]+cost[i], opt[i-2]+cost[i])
        #Return the min between opt[-1] and opt[-2]
        #as we can reach to the top for free either from the last step or the second to last step
        return int(min(opt[-1], opt[-2]))
