class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word.isupper():
            return True
        #if the string can pass the first condition 
        #it means the string consists of either all lowercase letters or 
        # capital and lowercase mixed letters, for the latter, only Google will pass, GooGle will not
        # so we only test from index 1 to len(word)-1
        for i in range(1, len(word)):
            if word[i].isupper():
                return False
        return True

    def detectCapitalUse2(self, word):
        #first letter is Uppercase
        n = len(word)
        #special for single letter string
        if n<= 1:
            return True
        
        if word[0].isupper():
            #second is upper case
            if word[1].isupper():
                for i in range(2, n):
                    if word[i].islower():
                        return False
            else:
                for i in range(2, n):
                    if word[i].isupper():
                        return False
        else:
            for i in range(1, n):
                if word[i].isupper():
                    return False
        return True

#test code:

