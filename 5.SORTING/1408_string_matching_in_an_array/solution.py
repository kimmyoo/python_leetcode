class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        
        words.sort(key=len)
        
        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                if words[i] in words[j] and words[i] not in res:
                    res.append(words[i])
        return res

s = Solution()
words = ["mass","as","hero","superhero"]
res = s.stringMatching(words)
print(res)