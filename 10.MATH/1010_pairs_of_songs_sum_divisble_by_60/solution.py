"""
In a list of songs, the i-th song has a duration of time[i] seconds. 
Return the number of pairs of songs for which their total duration in seconds is divisible by 60.  
Formally, we want the number of indices i < j with (time[i] + time[j]) % 60 == 0.
"""
import collections
class Solution:
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """        
        nums = [i % 60 for i in time]
        cnt = collections.Counter(nums)
        print(cnt)
        ans = 0
        
        for k in cnt.keys():
            print(k, cnt[k], cnt[60 - k])
            #cannot pair with itself
            if k == 30 or k == 0:
                ans += (cnt[k] * (cnt[k] - 1))
            elif 60 - k in cnt.keys():
                ans += (cnt[k] * (cnt[60 - k]))
        ans //= 2
        return ans


s = Solution()
time = [30,20,150,100,40]
res = s.numPairsDivisibleBy60(time)
print(res)


