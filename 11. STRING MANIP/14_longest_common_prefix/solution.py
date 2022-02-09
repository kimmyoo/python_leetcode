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
        #思路: 横向比较
        # 在list里找到最短的string的长度，
        # 将前一个string的[0:minLen]和后一个string的[0:minLen]进行比较
        # 如果一样不做任何处理
        # 如果不一样 minLen -= 1 同时check minLen 是不是到0 如果到0 要break out of the while loop
        # 最后返回 strs[0][:minLen]就可以
        # 注意前面处理 edge cases， eg. strs list 为 0个或1个元素

        # 知识点： min()函数可以有key argument 

        minLen= len(min(strs, key=len))
        
        if not strs or minLen==0:
            return ""
        if len(strs) == 1:
            return strs[0]

        i = 0
        while i < len(strs)-1:
            if strs[i][:minLen] == strs[i+1][:minLen]:
                i+=1
            else:
                i = 0
                minLen-=1
                if minLen == 0:
                    break
        return strs[0][:minLen]