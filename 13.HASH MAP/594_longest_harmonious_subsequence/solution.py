"""
We define a harmonious array as an array 
where the difference between its maximum value and its minimum value is exactly 1.
Now, given an integer array, 
you need to find the length of its longest harmonious subsequence 
among all its possible subsequences.
"""
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxLen = 0
        counter = {}
        #count occurrence of each number
        for e in nums:
            if e not in counter:
                counter[e] = 1
            else:
                counter[e] += 1
        #save keys(each distinct number) in a list and sort the list
        #remember to convert dict_key object to list object
        #CANNOT do this: keyList = counter.keys()
        keyList = list(counter.keys())
        keyList.sort()
        #I want to see whether the sum of occurrence of 
        #each number(e) and its neighbor(number that is 1 greater than e) 
        #is greater than maxLen(which is set to 0 initially)
        for e in keyList:
            if e + 1 in counter:
                s = counter[e] + counter[e+1]
                if s > maxLen:
                    maxLen = s
        return maxLen

s  = Solution()
nums = [1,3,2,2,5,2,3,7]
res = s.findLHS(nums)
print(res)
