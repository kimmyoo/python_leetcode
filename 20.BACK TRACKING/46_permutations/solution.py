class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        visited = set()
        self.backtrack(nums, visited, [], res)
        return res
        
    def backtrack(self, nums, visited, path, res):
        if len(path) == len(nums):
            res.append(path)
        #nums[i],as the beginning element, ranges from i to len(nums)
        for i in range(len(nums)):
            #this if condition is to eliminate the repeating element
            if i not in visited:
                visited.add(i)
                self.backtrack(nums, visited, path+[nums[i]], res)
                #backtracking step
                visited.remove(i)

s = Solution()
nums = [1, 2, 3]
res = s.permute(nums)
print(res)