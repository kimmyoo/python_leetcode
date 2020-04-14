"""
Rotate an array of n elements to the right by k steps.
For example, with n = 7 and k = 3,
the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different
ways to solve this problem.
"""

class Solution(object):
    def rotate(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: void Do not return anything, modify arr in-place instead.
        """
        # e.g. 
        # ['s','u', 'f', 'y', 'u']  k = 2
        n = len(arr)
        k = k % n # get the modulo
        # reverse entire list first, ==> u y f u s
        self.reverse(arr, 0, n - 1)
        # reverse the first half now, from 0 to k -1, ==> y u f u s 
        self.reverse(arr, 0, k - 1)
        # reverse the other half, k to n-1, ==> y u s u f
        self.reverse(arr, k, n - 1)
        
    # Questions: how to reverse a string?
    # answer: s = s[::-1]
    def reverse(self, arr, i, j):
        """reverse a list"""
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    def rotate2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        l = len(nums)
        k %= l
        res = nums[len(nums)-k:]
        res.extend(nums[:len(nums)-k])
        for i in range(l):
            nums[i] = res[i]
    
    def rotate3(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        Using Cyclic Replacements
        """
        
        count, start = 0, 0
        l = len(nums)
        k = k % l
        while count < l:
            current = start
            prev = nums[start]
            while True:
                print(start)
                next = (current+k) % l
                temp = nums[next]#save the ele in next spot
                nums[next] = prev
                prev = temp
                current = next
                count += 1
                if start == current:
                    break
            start += 1

# test goes here
arrayList = ['s','u', 'f', 'y', 'u']
print ("original array list is:\n", arrayList)
s = Solution()
s.rotate(arrayList, 2)
print("offset k is 2, array list becomes: \n", arrayList)
