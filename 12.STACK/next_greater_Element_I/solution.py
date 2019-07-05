"""
You are given two arrays (without duplicates) nums1 and nums2
here nums1's elements are subset of nums2. Find all the next 
greater numbers for nums1's elements in the corresponding places of nums2.
The Next Greater Number of a number x in nums1 is the first greater number 
to its right in nums2. If it does not exist, output -1 for this number.

Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
"""

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        for num in nums1:
            found = False
            i = 0
            while num != nums2[i]:
                i+=1
            for j in range (i+1, len(nums2)):
                if nums2[j] > num:
                    res.append(nums2[j])
                    found = True
                    break
                j+=1
            if not found:
                res.append(-1)
        return res

    # leet code solution using stack 没看
    def nextGreaterEle(self, nums1, nums2):
        d = {}
        st = []
        ans = []
        
        for x in nums2:
            while len(st) and st[-1] < x:
                d[st.pop()] = x
            st.append(x)

        for x in nums1:
            ans.append(d.get(x, -1))
            
        return ans



#test code
s = Solution()
nums1 = [4,1,2]
nums2 = [1,3,4,2]
res = s.nextGreaterElement(nums1, nums2)
res2 = s.nextGreaterEle(nums1, nums2)
print(res)
print(res2)


