"""
Given a sorted array nums, remove the duplicates in-place such that each 
element appear only once and return the new length.Do not allocate extra 
space for another array, you must do this by modifying the input array 
in-place with O(1) extra memory.
"""

class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, sorted_arr):
        if not sorted_arr:
            return 0
        if len(sorted_arr) == 1:
            return 1
        
        j = 0  # Position of last processed non-duplicate
        n = len(sorted_arr)
        for i in range(1, n):
            if sorted_arr[i] != sorted_arr[j]:
                sorted_arr[j + 1] = sorted_arr[i]
                j += 1
        return j + 1


# j=0             n = 4
# 1, 2, 2, 3


# j  i            i = 1
# 1, 2, 2, 3

#    j  i         i = 2
# 1, 2, 2, 3

#    j,    i      i = 3
# 1, 2, 2, 3 


# 1, 2, 3
#       j=2


#test code
testArray = [0, 1, 2, 3, 3, 4, 4, 5, 5, 5, 6]
oldLen = len(testArray)
s = Solution()
newLength =s.removeDuplicates(testArray)
print ("new length of array:", newLength)

print ("new array:")
for i in range (newLength):
    print (testArray[i])

print("what's left in orignal array:")
for n in range(oldLen):
    print (testArray[n])
