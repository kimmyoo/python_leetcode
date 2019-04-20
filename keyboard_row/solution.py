class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        s1 = set(['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'])
        s2 = set(['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'])
        s3 = set(['z', 'x', 'c', 'v', 'b', 'n', 'm'])
        
        #important, here I used reversed() because you cannot remove an element
        #while iterating over a list
        #The reason for this is that the iterator does not know that a list element 
        #was removed, and happily advances to the next item.
        for word in reversed(words):
            numOfFlags = 0
            flags = [False, False, False]
            for c in set(word.lower()):
                if c in s1:
                    flags[0] = True
                elif c in s2:
                    flags[1] = True
                elif c in s3:
                    flags[2] = True
            for flag in flags:
                if flag == True:
                    numOfFlags +=1
            if numOfFlags > 1:
                words.remove(word)
            print(flags)
        return words

s = Solution()
inputList =["abdfs","cccd","a","qwwewm"]
res = s.findWords(inputList)
print(res)