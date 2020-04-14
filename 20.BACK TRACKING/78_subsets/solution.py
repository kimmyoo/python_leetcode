class Solution:
    def subsets(self, nums):
        #k is the current length of subset
        #C(n, k)
        def dfs(k, start, curr):
            if len(curr) == k:
                res.append(curr[:])# cannot pass a reference curr to append(), must be a copy
                return
            # for loop is to select the next ele from remaining eles in nums 
            # to add to current subset
            for i in range(start, l):
                curr.append(nums[i])
                dfs(k, i + 1, curr)
                curr.pop()#backtracking


        res = []
        l = len(nums)
        # k is the length of the subset, so its range is 0 - len(nums)
        for k in range(l + 1):
            dfs(k, 0, [])
        return res

s = Solution()
nums = [0, 1, 2]
res = s.subsets(nums)
print(res)