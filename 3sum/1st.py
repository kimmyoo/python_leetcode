"""my attempt after seeing the solution 
on 11/26/17"""

class Solution(object):
	def threeSum (self, nums):
		nums.sort()
		res = []
		
		for i in range (len(nums)-2):
			if i == 0 or i > 0 and nums[i-1] != nums[i]:
				left = i + 1
				right = len(nums) - 1
				while left < right:
					sum = nums[i] + nums [left] + nums[right]
					if sum == 0:
						res.append([nums[i], nums[left], nums[right]])
						left += 1
						right -= 1
						while left < right and nums[left-1] == nums[left]:
							left += 1
						while left < right and nums[right+1] == nums[right]:
							right += 1
					elif sum < 0:
						left += 1
					else:
						right -= 1
		return res


intlist = [4, -4, 0, 9, -9, 0]
sol = Solution()
res = sol.threeSum(intlist)
print (res)
