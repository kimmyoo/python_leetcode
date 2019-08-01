"""
Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's, 
and all the 0's and all the 1's in these substrings are grouped consecutively.
Substrings that occur multiple times are counted the number of times they occur.

Example 1:
Input: "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of 
consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".

HINT:
Let's try to count the number of valid binary strings between groups[i] and groups[i+1]. 
If we have groups[i] = 2, groups[i+1] = 3, then it represents either "00111" or "11000". 
We clearly can make min(groups[i], groups[i+1]) valid binary strings within this string. 
Because the binary digits to the left or right of this string must change at the boundary, 
our answer can never be larger.
"""
class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        #since we started from index 1, 
        #as default, position has an element, either '1' or '0'
        #so the groups will be initiated with 1 at its 0 index
        groups = [1]
        for i in range(1, len(s)):
            if s[i-1] == s[i]:
                #update the last ele in list
                groups[-1] +=1
            else:
                groups.append(1)
        
        res = 0
        
        for j in range(len(groups)-1):
            res += min(groups[j], groups[j+1])
        return res

#test
s = Solution()
testStr = "00111"
res = s.countBinarySubstrings(testStr)
print (res)