import collections

class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        cnt = collections.Counter(words[0])

        for word in words[1:]:
            cnt2 = collections.Counter(word)
            for k in cnt.keys():
                cnt[k] = min(cnt[k], cnt2[k])
        # elements() returns itertool of all the known elements in the Counter object
        # if an element appear 0 times then that element will not be returned
        return list(cnt.elements())

s = Solution()
words = ["bella","label","roller"]
res = s.commonChars(words)
print(res)