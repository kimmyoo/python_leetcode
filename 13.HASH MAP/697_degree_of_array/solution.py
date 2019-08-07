"""
Given a non-empty array of non-negative integers nums, 
the degree of this array is defined as the maximum frequency of any one of its elements.
Your task is to find the smallest possible length of a (contiguous) subarray of nums, 
that has the same degree as nums.

Input: [1, 7, 7, 5, 7, 1]
Output: 4
Explanation: The degree of this array is 3 because 7 appears the most of any number. 
The shortest subarray that you can make that has a degree of 3 is [7,7,5,7]. 
The length of that subarray is 4, so we return 4.
"""

class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #for saving frequency of each element
        dFreq = {}
        #for saving min and max index of the same element
        dMinMax = {}
        #n is a counter to remember the index of current element
        #CANNOT use index() function since index() returns the first appearance of 
        #repeating elements.
        n, minLen = 0, len(nums)
 
        for e in nums:
            if e in dFreq:
                dFreq[e]+=1
                #if the element has been seen before update its maxindex to n
                dMinMax[e][1] = n
            else:
                dFreq[e]=1
                dMinMax[e] = [n, n]
            n+=1
         
        degreeOfArray = max(dFreq.values())
        #print(dFreq, dMinMax, degreeOfArray)
        
        for e in dFreq:
            if dFreq[e] == degreeOfArray:
                if (dMinMax[e][1]-dMinMax[e][0] +1) < minLen:
                    minLen = dMinMax[e][1] - dMinMax[e][0] +1
        return minLen

#test 