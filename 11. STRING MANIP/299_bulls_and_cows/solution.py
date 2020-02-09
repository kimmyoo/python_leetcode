import collections

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        cSecret = collections.Counter(secret)
        sSet = set(secret)
        gSet = set()
        numOfBulls, numOfCows = 0, 0
        
        for ch in guess:
            if ch in sSet:
                numOfCows+=1
            
            if ch not in gSet:
                gSet.add(ch)
            #this is to deal with repeating elements in guess
            else:
                #this if condition is needed to deal with 
                #repeating elements in secret
                if cSecret[ch] == 1:
                    numOfCows-=1
                else:
                    cSecret[ch]-=1
        
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                numOfBulls+=1
                numOfCows-=1

        return "%dA%dB"%(numOfBulls, numOfCows)
    
s = Solution()
res = s.getHint("0012", "1234")
print(res)
