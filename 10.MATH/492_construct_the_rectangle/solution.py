class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        #turn w into integer first
        w = int(math.sqrt(area))
        while area % w != 0:
            w -= 1
        # [Length, Width]
        return [area / w, w]


