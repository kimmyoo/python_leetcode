"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
Your algorithm should run in O(n) complexity.

Example:
Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""

class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        if not num:
            return 0
        d = {}
        # the following for loop will get rid of duplicates and 
        # keep distinct element in dictionary
        for e in num:
            if e not in d:
                d[e] = 1
        # default value of res is 1
        res = 1
        print (d)
        
        for c in num:
            current = 1
            #the following two lines are for repetitive list elements
            if c not in d:
                continue
            # to see if there exists an element less than c and find the lower end 
            while c - 1 in d:
                c -= 1
            # print("current c:", c)
            del d[c]# remember to delete the lower end once hit the lower end
            #print(d)
            
            # to see if there eixists an element that is greater than current c by 1 
            # and update current
            while c + 1 in d:
                c += 1
                current += 1
                #print(current)
                del d[c]
            res = max(res, current) # this line is update the maximum value to res. 
        return res

# test code goes here~
s = Solution()
inputList = [100, 4, 100, 200, 1, 3, 2]
print (s.longestConsecutive(inputList))

# notes：
# use dictiontary to keep distinct elements
# find lower end and go back the higher end and update current value. 
# don't forget to use max() update the res value. 
# don't forget empty list scenario. 
# remember to deal with repetitive elements in the list. 
