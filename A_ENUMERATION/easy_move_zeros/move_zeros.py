"""
moving 0s to the end of the list in place
"""

# 思路：
# enumerate....and use j to loop thru the list
# if element is not 0, j and index both increment 
# if element is 0, j stays, but enumerate keeps incrementing index
# to next element, if that element is not 0, then swap will be
# performed betwen 0 and non 0 elements.
# and j always points to the first 0 in the list. 

#  example:

#  j,index                              j = 0, index = 0
#   0，     9   0    1     1     0

#   j    index                          j = 0, index = 1
#   0       9   0    1     1     0
                                    # first swap happens here
#           j  index                    j = 1, index = 2
#   9       0   0    1     1     0 

#           j      index                j = 1, index = 3
#   9       0   0    1     1     0 

#               j         index
#   9       1   0    0     1     0 

#                    j          index
#   9       1    1   0     0     0


# j increments after swapping; index always increments.
class Solution:
    def moveZeros(self, nums):
        j = 0
        for index, element in enumerate(nums):
            if element != 0:
                nums[index], nums[j] = nums[j], nums[index]
                print ("swap") # for test purpose
                j+=1
    
# test 
s = Solution()
nums = [4, 0, 0, 2, 0, 5, 2]
s.moveZeros(nums)
print (nums)
