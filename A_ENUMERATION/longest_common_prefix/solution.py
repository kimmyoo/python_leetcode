"""Write a function to find the longest common prefix string amongst 
an array of strings."""
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:# if list is empty
            return ""
        res = strs[0]#set res to the first string in the list
        #for loop starting from the second string in the list
        #using list slicing
        for s in strs[1:]:
            n = len(s)
            # enumerate on string: i is the index; c is the character
            for i, c in enumerate(res):
                #if length of previous string exceeds the latter
                #or a mismatch occures
                if i >= n or res[i] != s[i]:
                    #reassign res by using string slicing
                    res = res[:i]
                    break # this breaks inner for loop
        return res

s = Solution()
test_list = ["RoSeWira", "RoSe", "RoSurvival", "RoSe<3"]
test_list2 = ["yao", "ling tosite sigure", "enigmatic feeling"]
print ("longest prefix is:", s.longestCommonPrefix(test_list))
# if mismatch occurs on every first letter, res is finally assigned
# by res[0:0] which is an empty string "" 
print ("longest prefix is:", s.longestCommonPrefix(test_list2))
