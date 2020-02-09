# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
# 
# Example 1:
# 
# Input: ["flower","flow","flight"]
# Output: "fl"


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        
        minLen = float("inf")
        
        for str in strs:
            minLen = min(minLen, len(str))
        if minLen == 0:
            return ""
        
        i = 0
        while i < len(strs)-1:
            if strs[i][:minLen] == strs[i+1][:minLen]:
                i+=1
            else:
                i = 0
                minLen-=1
                #this break statement is important
                if minLen == 0:
                    break
        return strs[0][:minLen]