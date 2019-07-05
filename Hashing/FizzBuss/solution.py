class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        for i in range (1, n+1):
            flag_div_by_3 = (i % 3 == 0)
            flag_div_by_5 = (i % 5 == 0)
            currentString  = ""
            
            if flag_div_by_3:
                currentString += "Fizz"
            if flag_div_by_5:
                currentString += "Buzz"
            if not currentString:
                currentString = str(i)
            res.append(currentString)
        return res

#testing code
s = Solution()
res = s.fizzBuzz(15)
print(res)


"""
LEARN HOW TO HASH IT
"""