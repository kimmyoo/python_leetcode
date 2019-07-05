"""
Given a string S, return the "reversed" string where all characters 
that are not a letter stay in the same place, and all letters reverse their positions.
"""

class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        stringList = list(S)
        head = 0
        tail = len(S) -1 
        while head <= tail:
            if not stringList[head].isalpha():
                head+=1
                continue
            if not stringList[tail].isalpha():
                tail-=1
                continue
            if stringList [head] != stringList[tail]:
                temp = stringList[tail]
                stringList[tail] = stringList[head]
                stringList[head] = temp
            head+=1
            tail-=1
        res = ""
        for e in stringList:
            res += e
        return res

#test code
s = Solution()
testString = "-!12jinyao?"
res = s.reverseOnlyLetters(testString)
print(res)

