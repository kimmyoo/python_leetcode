"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one
sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m
+ n) to hold additional elements from nums2. The number of elements
initialized in nums1 and nums2 are m and n respectively.

"""


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # tips: comparison takes place in reversed order
        i = m - 1
        j = n - 1
        k = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
                print ("haha")
            else:
                nums1[k] = nums2[j]
                j -= 1
                print ("hehe")
            k -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
            print("yoyo")

# test code 
num1 = [0]*20
for n in range(7):
    num1[n] = 2*n
print (num1)
num2 = [n*2-5 for n in range (1, 11)]
print (num2)
m = 7
n = len(num2)
s = Solution()
s.merge(num1, m, num2, n)
print (num1)
