"""
Given two positive integers x and y, 
an integer is powerful if it is equal to x^i + y^j for some integers i >= 0 and j >= 0.
Return a list of all powerful integers that have value less than or equal to bound.
You may return the answer in any order.  
In your answer, each value should occur at most once.
"""
class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        #if bound == 0:
            #return []
        xList, yList= [1], [1]
        curX, curY = x, y
        
        #left end 1 cannot be ommited 
        #otherwise infinite loop
        while 1 < curX < bound:
            xList.append(curX)
            curX *= x
        
        while 1 < curY < bound:
            yList.append(curY)
            curY *= y
        resSet = {x+y for x in xList for y in yList if x + y <= bound }
        res = list(resSet)
        return res

