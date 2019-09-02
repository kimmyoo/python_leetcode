"""
Write an algorithm to determine if a number is "happy".
A happy number is a number defined by the following process: 
Starting with any positive integer, replace the number by the sum of the squares of its digits, 
and repeat the process until the number equals 1 (where it will stay), 
or it loops endlessly in a cycle which does not include 1. 
Those numbers for which this process ends in 1 are happy numbers.

example:
Input: 19
Output: true
Explanation: 
1**2 + 9**2 = 82
8**2 + 2**2 = 68
6**2 + 8**2 = 100
1**2 + 0**2 + 0**2 = 1

typical ways of playing with digits
method 1:
    temp = 0
    while n > 0:
        digit = n % 10
        n = n/10
        temp += digit**2 #play with digit

method 2:
numString = str(num)
for digit in numString:
    play w/ int(digit)
"""
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #this is how to deal with possible infinite loop or recursion, use a hash set.
        numSet = set()
        while n !=1:
            n = sum([int(digit)**2 for digit in str(n)])
            if n not in numSet:
                numSet.add(n)
            else:
                return False
        return True

s = Solution()
res1 = s.isHappy(19)
res2 = s.isHappy(18)
print(res1, res2)


