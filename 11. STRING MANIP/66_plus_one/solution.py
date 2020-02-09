class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        l = len(digits)
        num, res = 0, []
        for i in range(l):
            num = num + digits[i] * 10**(l-i-1)
        
        num += 1
        num = str(num)

        for ch in num:
            res.append(ch)
        return res
