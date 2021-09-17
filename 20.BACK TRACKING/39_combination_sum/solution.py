class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        
        def backtracking(arr, target, path):
            # 2 terminating cases
            if target < 0:
                return
            if target == 0:
                res.append(path)
                return
            for i in range(len(arr)):
                if arr[i] > target:
                    continue
                backtracking(arr[i:], target-arr[i], path+[arr[i]])
        
        backtracking(candidates, target, [])
        
        return res

s = Solution()
candidates = [8, 3, 4, 6, 2, 7, 3]
target = 13
ans = s.combinationSum(candidates, target)
print(ans)
