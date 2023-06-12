"""
Given an array A of strings made only from lowercase letters, 
return a list of all characters that show up in all strings within the list 
(including duplicates).  For example, if a character occurs 3 times in 
all strings but not 4 times, you need to include that character three 
times in the final answer.

You may return the answer in any order.
Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: ["cool","lock","cook"]
Output: ["c","o"]
"""
class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        res_set = set(A[0])
        arr_size = len(A)
        count_dict = {}
        res = []
        
        # find intersection set
        for i in range(1, arr_size):
            res_set = set(A[i]) & res_set
            if len(res_set)!= 0:
                i+=1
        # find frequency of each char and use a dict to record 
        for char in res_set:
            count = A[0].count(char)
            for i in range(1, arr_size):
                count = min(A[i].count(char), count)
                i+=1
            count_dict.update({char: count})
        # append each char to res according to frequency of each char
        for key in count_dict:
            for i in range(0, count_dict[key]):
                res.append(key)
        return res
    
    def commonChars2(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        # for counting occurence of each letter
        d = {}
        commonSet = set(words[0])
        res = []

        # loop thru list and find intersection of each individual word
        # if no intersection, return a empty []
        for i in range(1, len(words)):
            commonSet = commonSet & set(words[i])
            # if there is intersection
            if len(commonSet) != 0:
                i += 1
            else:
                return []
        
        for letter in commonSet:
            commonCount = words[0].count(letter)
            for i in range(1, len(words)):
                commonCount = min(commonCount, words[i].count(letter))
            d[letter] = commonCount

        for key in d:
            for i in range(0, d[key]):
                res.append(key)
        return res
#test
s = Solution()
arr = ["boomtt", "boatt", "aboutt"]
res = s.commonChars(arr)
print(res)
