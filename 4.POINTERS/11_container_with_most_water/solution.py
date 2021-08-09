class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        mxArea = 0
        l, r = 0, len(height) -1 
        while l != r:
            x = abs(r-l)
            y = min(height[l], height[r])
            mxArea = max(mxArea, x*y)
            if height[l] <= height[r]:
                l+=1
            else:
                r-=1

        return mxArea
            
s = Solution()
height = [1, 4, 2, 5, 10, 3, 9, 10, 34, 4]
res = s.maxArea(height)
print(res)