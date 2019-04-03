class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        if x == y:
            return 0

        temp = x ^ y
        dis = 0
       
        while temp != 0:
            # bit and operation to determin lowest bit is 1 or 0
            if (temp & 1):
                dis += 1
            # bit right shift, when shifting, 0 is inserted to current position
            temp = temp >> 1
        return dis


s = Solution()
dis = s.hammingDistance(66, 95)
print(dis)
