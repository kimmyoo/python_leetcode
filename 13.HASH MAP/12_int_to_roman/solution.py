from collections import OrderedDict

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        # if you need an ordered dictionary, (OrderedDict will remember the insertion order)
        # from python3.6 the default dictionary object is Ordered.
        # you need to pass a list of tuple to OrderedDict constructor in order
        d = [
            (1000, 'M'), 
            (900, 'CM'), 
            (500, 'D'), 
            (400, 'CD'), 
            (100, 'C'), 
            (90,'XC'), 
            (50, 'L'), 
            (40, 'XL'), 
            (10, 'X'), 
            (9, 'IX'), 
            (5, 'V'), 
            (4, 'IV'), 
            (1, 'I')]
        
        translation = OrderedDict(d)
        
        res = ""
        
        for i in translation:
            res += (num//i) * translation[i]
            num %= i

        return res

s = Solution()
res = s.intToRoman(87)
print(res)