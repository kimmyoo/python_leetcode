import string

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        exclude = set(string.punctuation)
        #replace punctuation with ' ' in case the string is like "a,a,a, b, c, c"
        for ch in exclude:
            paragraph = paragraph.replace(ch, ' ') #
        paraList = list(paragraph.split()) #Default value is a whitespace
        freqDict, freq = {}, 0
        
        for word in paraList:
            word = word.lower() # change to lower before updating freqDict
            if word not in banned:
                if word not in freqDict:
                    freqDict[word] = 1
                else:
                    freqDict[word] += 1
                if freqDict[word] > freq:
                     freq = freqDict[word]  

        for k, v in freqDict.items():
            if v == freq:
                return k

s = Solution()
paragraph = "Bob. hIt, baLl"
banned = ["bob", "hit"]
res = s.mostCommonWord(paragraph, banned)
print(res)