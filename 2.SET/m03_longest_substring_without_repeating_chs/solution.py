"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3.
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        i, j = 0, 0
        mx = 0
        hashSet = set()
        while j < len(s):
            #within the while loop, the adding and the deletion of a ch in current set
            #is control by if ... else... logic
            # if a char in set already, remember to delete the repeating ch which appears at index i
            # in next loop, you will add the same char in the set
            if s[j] not in hashSet:
                hashSet.add(s[j])
                mx = max(mx, len(hashSet))
                j+=1
            else:
                hashSet.remove(s[i])
                i+=1
        return mx


s = Solution()
res = s.lengthOfLongestSubstring("abcdefffvfffgacdejin")
print(res)