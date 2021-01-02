class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        #enumerate(iterable, start)
        #split()
        #enumerate second parameter is start index
        for idx, word in enumerate(sentence.split(), 1):
            if word.startswith(searchWord):
                return idx
        return -1