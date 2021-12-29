import collections

class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        l = [ch.lower() for ch in licensePlate if ch.isalpha()]
        d = collections.Counter(l)
        candidates = []
        words.sort(key=len)
        for word in words:
            tempD = collections.Counter(word)
            add = False
            for k, v in d.items():
                if k in tempD and v <= tempD[k]:
                    add = True
                else:
                    add = False
                    break
            if add:
                candidates.append(word)
        return candidates[0]

s = Solution()
license = "1s3 456"
words = ["looks","pest","stew","show"]

res = s.shortestCompletingWord(license, words)
print(res)