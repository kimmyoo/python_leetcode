"""

Given n points in the plane that are all pairwise distinct, 
a "boomerang" is a tuple of points (i, j, k) such that the distance 
between i and j equals the distance between i and k (the order of the tuple matters).

The key insight here is that if we have a list of n points [p1, p2, p3, ..., pn] 
then there are nP2 = (n! / (n-2)!) = n*(n-1) pairs of points that can follow p in order to form a boomerang.
"""
class Solution(object):
    def getDistSqr(self, p1, p2):
        return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2
    
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in range(len(points)):
            d = {}
            for j in range(len(points)):
                if i == j:
                    continue
                dist = self.getDistSqr(points[i], points[j])
                if dist not in d:
                    d[dist] = 1
                else:
                    d[dist] +=1
            #we only care about points with same distance to points[i]
            for k in d:
                if d[k] > 1:
                    #nP2 = (n! / (n-2)!) = n*(n-1)
                    res += d[k] * (d[k]-1)
        return res