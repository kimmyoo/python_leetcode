#===============================================================================
# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
#===============================================================================

class Solution(object):
    def isAlienSorted(self, words, order):
        indexDic = {c:i for i, c in enumerate(order)}
        #for...else 
        #the else clause executes only if the for loop completes normally (didn't encounter break)
        for n in range(len(words)-1):
            word1 = words[n]
            word2 = words[n+1]
            for m in range(min(len(word1), len(word2))):
                # If they compare badly, it's not sorted.
                if word1[m] != word2[m]:
                    if indexDic[word2[m]] < indexDic[word1[m]]:
                        return False
                    break
            # If we didn't find a first difference, the
            # words are like ("app", "apple").
            else:
                if len(word1) > len(word2):
                    return False
        return True

#test code
s = Solution()
words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
res = s.isAlienSorted(words, order)
print (res)