"""
Assume you are an awesome parent and want to give your children some cookies. 
But, you should give each child at most one cookie. 
Each child i has a greed factor gi, which is the minimum size of a cookie that the child will be content with; 
and each cookie j has a size sj. If sj >= gi, 
we can assign the cookie j to the child i, and the child i will be content. 
Your goal is to maximize the number of your content children and output the maximum number.

Note:
You may assume the greed factor is always positive. 
You cannot assign more than one cookie to one child.
"""
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        lenG = len(g)
        lenS = len(s)
        
        if lenG ==0 or lenS == 0:
            return 0
        
        g.sort()
        s.sort()
        i, j = 0, 0
        res = 0
        
        while i <= lenG-1 and j <= lenS-1:
            if s[j] >= g[i]:
                res +=1
                i+=1
                j+=1
            else:
                j+=1
        
        return res
        
#test
sol = Solution()
g = [1,2]
s = [1,2,3]
res = sol.findContentChildren(g, s)
print(res)
