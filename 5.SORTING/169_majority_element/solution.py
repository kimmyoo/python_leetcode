class Solution(object):
    """
    my solution
    """
    def majorityElementA(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # sorting takes extra space
        nums.sort()
        count = len(nums)//2
        if count == 0:
            return nums[0]
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                count-=1
                if count <= 0:
                    return nums[i]
            else:
                count = len(nums)//2
    """
    leetcode method1:
    If the elements are sorted in monotonically increasing (or decreasing) order, the majority element can be found at index
    n//2
    """
    def majorityElementB(self, nums):
        nums.sort()
        return nums[len(nums)//2]
    
    """
    leetcode method2:
    hashmap 
    time: O(n), a whole iteration through the list
    space: O(n)  at most n/2 key: value associations
    """
    def majorityElementC(self, nums):
        d = dict()
        for ele in nums:
            if ele in d:
                d[ele] += 1
            else:
                d[ele] = 1
        """learn this to get key that associated with the max value of a dict!!!"""
        return max(d, key = d.get)


#test 
s = Solution()
nums = [1, 2, 2, 0, 0, 0, 0, 3, 0]
res1 = s.majorityElementA(nums)
res2 = s.majorityElementB(nums)
res3 = s.majorityElementC(nums)
print(res1, res2, res3)

