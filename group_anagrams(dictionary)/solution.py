"""
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:
For the return value, each inner list's elements must follow the lexicographic
order.
All inputs will be in lower-case.

"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {} # initiate an dictionary to hold key: value pairs
        res = [] # initiate a list to hold result 
        for s in strs:
            k = self.make_key(s)
            if k not in d:
                # here d[k] must be assigned by a list i.e [s]
                # to enable the append() function
                d[k] = [s] 
            else:
                d[k].append(s)
        #loop through the dicionary to append the inner lists to res
        for k in d:
            res.append(sorted(d[k])) # sorted() ensures the lexicographic order
        return res

    # make_key() will match multiple potential strings to one key
    # which is the ordered string in lexicographic order
    def make_key(self, s):
        return ''.join(sorted(s))


s = Solution()
input_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
print (s.groupAnagrams(input_list))
