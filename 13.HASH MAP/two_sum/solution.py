class Solution1(object):
    def twoSum(self, nums, target):
        d = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in d:
                return [d[m], i]
            else:
                d[n] = i






#test code
s1 = Solution1()
nums1 = [2, 3, 5, 1, 0]
#this test case is for duplicate elements
nums2 = [6, 0, 6]
target1 = 4
target2 = 12
res1 = s1.twoSum(nums1, target1)
print(res1)
res2 = s1.twoSum(nums2, target2)
print(res2)


