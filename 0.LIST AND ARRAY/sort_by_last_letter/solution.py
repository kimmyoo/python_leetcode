class Solution:
    def sortByLastLetter(self, sentence:str) -> list:
        words = sentence.split(' ')
        # key is a lambda function
        words.sort(key=lambda word: word[-1].lower())
        return words

s = Solution()
res = s.sortByLastLetter("wO shI aI wo eI da ye")
print(res)