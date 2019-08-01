class Solution(object):
    def get_intersection(self, set1, set2):
        # len(set1) < len(set2) will ensure 
        # if condition is less tested
        return [x for x in set1 if x in set2]
    
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1, set2 = set(nums1), set(nums2)
        if len(set1) < len(set2):
            return self.get_intersection(set1, set2)
        else:
            return self.get_intersection(set2, set1)

#test code
s = Solution()
nums1 = [1, 2, 3, 4]
nums2 = [3, 4, 0]
res = s.intersection(nums1, nums2)
print(res)