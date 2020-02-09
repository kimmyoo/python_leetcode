"""
We define the Perfect Number is a positive integer 
that is equal to the sum of all its positive divisors except itself.
Now, given an integer n, write a function that returns true 
when it is a perfect number and false when it is not.
"""
import math
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False

        root = math.sqrt(num)
        root = int(math.floor(root))
        divisors = []
        for i in range(1, root+1):
            if num%i == 0:
                divisors.append(i)
                divisors.append(num//i)
        divisors.remove(num)
        print(divisors)
        return num == sum(divisors)
