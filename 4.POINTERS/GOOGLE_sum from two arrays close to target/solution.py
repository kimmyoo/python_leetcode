"""
A and B are two arrays, find a tuple of values from A and B respectively 
and their sum is the closest to target
[5, 9, 6, 3, 7, 10, 2]  
[11, 2, 6, 5, 4, 1, 7], target = 19, algorithm should return (7, 11)

2, 3, 5, 6, 7, 9, 10
1, 2, 4, 5, 6, 7, 11
"""

class Solution(object):
    def getPair(self, A, B, target):
        """
        typeA: list
        typeB: list
        type target: int
        rtype: tuple
        """
        sA = sorted(A)
        sB = sorted(B)
        minAbs = abs(sA[0] + sB[0] - target) 
        t = (sA[0], sB[0])
        ptrA, ptrB = 0, len(sB)-1

        while ptrA <= len(sA) -1 and ptrB >= 0:
            curDiff= sA[ptrA] + sB[ptrB] - target
            #we use abs() to decide minAbs
            if abs(curDiff) < minAbs:
                minAbs = min(abs(curDiff), minAbs)
                t = (sA[ptrA], sB[ptrB])
            #we use diff to decide which ptr needs to be moved
            if curDiff == 0:
                return (sA[ptrA], sB[ptrB])
            elif curDiff > 0:
                ptrB-=1
            else:
                ptrA+=1
        return t


s = Solution()
A = [5, 9, 6, 3, 7, 10, 2]
B = [11, 2, 6, 5, 4, 1, 7]
target = 19
res = s.getPair(A, B, target)
print(res)