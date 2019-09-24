class Solution1(object):
    #space complexity: O(n),  n elements, n items stored in hash map 
    #time complexity: O(n), each lookup in map costs O(1)
    def twoSumA(self, nums, target):
        """
        :type nums: list
        :type target: int
        :rtype: list
        """
        d = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in d:
                return [d[m], i]
            else:
                d[n] = i


    # time complexity is O(n**2)
    # space complexity O(1)
    def twoSumB(self, nums, target):
        """
        :type nums: list
        :type target: int
        :rtype: list
        """
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

#test code
s1 = Solution1()
nums1 = [2, 3, 5, 1, 0]
nums2 = [6, 0, 6] #this test case is for duplicate elements
target1 = 4
target2 = 12
res1 = s1.twoSumA(nums1, target1)
res2 = s1.twoSumB(nums1, target1)
res3 = s1.twoSumA(nums2, target2)
res4 = s1.twoSumB(nums2, target2)
print(res1, res2, res3, res4)