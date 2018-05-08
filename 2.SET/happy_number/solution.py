"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any
positive integer, replace the number by the sum of the squares of its digits,
and repeat the process until the number equals 1 (where it will stay), or it
loops endlessly in a cycle which does not include 1. Those numbers for which
this process ends in 1 are happy numbers.

Example: 19 is a happy number

1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
"""

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        tank = set()
        while True:
            if n not in tank:
                tank.add(n)
                # learning objective: 
                # num -> string -> num; list comprehension
                n = sum([int(x)*int(x) for x in list(str(n))])
                if n == 1:
                    return True 
            else:
                return False 
            

# knowledge point: list(), list comprehension, set()
# tank = set()与 if n in tank: 的搭配使用
example_num = 1234
example_list = [int(x)*int(x) for x in list(str(example_num))]
print (example_list)

s = Solution()
print(s.isHappy(23))

