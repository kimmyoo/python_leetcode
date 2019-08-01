"""
There are 2N people a company is planning to interview. 
The cost of flying the i-th person to city A is costs[i][0], 
and the cost of flying the i-th person to city B is costs[i][1].

Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.
Example 1:
Input: [[10,20],[30,200],[400,50],[30,20]]
Output: 110

hint: greedy algorithm
take each minimum cost and add it up to sum, record difference at the same time if the other cost is selected, 
sort the differences and add the least cost accordingly back to sum len(diff) - n times
问题分析：
（1）先理解题目，就是有2N人去面试，共有A、B两个城市，每个城市去N人，然后是达到花费最少。题目已经提示贪心算法。
（2）第一步，先不考虑去每个城市的人数，每次选择最优的城市去，即可（贪心思想），此时，并记录，如果去另外一个城市多出的花费。例如，去A要10，去B要20，那就现在优先考虑去A，然后开辟一个数组，记录此时如果去B的差价，很显然是10。
（3）现在开始分析，是不是两个城市都去了N人，如去A城市的人多了，说明要从中选取多余的人改去B城市，现在怎么选择哪？利用之前记录的差价，进行排序，依次从最小的开始进行改去B市，其中这也是贪心思想。同理，去B市的人多了，就选择一部去A市。
"""
class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        sum = 0
        n = len(costs)//2
        diffa = []
        diffb = []
        
        for cost in costs:
            if cost[0] < cost[1]:
                sum += cost[0]
                diffb.append(cost[1]-cost[0])
            else:
                sum += cost[1]
                diffa.append(cost[0]-cost[1])
        # num of ppl going to A is more than num of ppl going to B
        if len(diffb) > len(diffa):
            diffb.sort()
            for i in range(len(diffb)-n):
                sum += diffb[i]
        else:
            diffa.sort()
            for j in range(len(diffa)-n):
                sum += diffa[j]
        return sum

#test code[[10,20],[30,200],[400,50],[30,20]]
s = Solution()
costs = [[10,20],[30,200],[400,50],[30,20]]
res = s.twoCitySchedCost(costs)
print (res)