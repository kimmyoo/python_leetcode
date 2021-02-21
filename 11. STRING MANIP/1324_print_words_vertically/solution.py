class Solution(object):
    def printVertically(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        """knowledge point: 
            str.ljust(length, "char")
            str.rstrip()
        """
        sList = s.split()
        formattedList = []
        res = []
        maxLen = 0
        #get the max length of input words
        for word in sList:
            maxLen = max(maxLen, len(word))
        
        #padding words with trailing spaces
        for word in sList:
            word = word.ljust(maxLen, " ")
            formattedList.append(word)
        
        #for loop to construct each word vertically
        #rstrip() all trailing spaces before appending to res
        for i in range(maxLen):
            word = ''
            for j in range(len(sList)):
                word += formattedList[j][i]
            res.append(word.rstrip())
        return res

obj = Solution()
ans = obj.printVertically("print words vertically")
print(ans)