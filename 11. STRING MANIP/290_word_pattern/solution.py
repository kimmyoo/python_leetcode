class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        strList = str.split()
        l = len(pattern)
        
        if len(strList) != l:
            return False

        d, i = {}, 0
        for i in range(l):
            if pattern[i] not in d:
                d[pattern[i]] = strList[i]
            else:
                if d[pattern[i]] != strList[i]:
                    return False
        
        pCount, sCount = len(set(pattern)), len(set(strList))
        
        if pCount!= sCount:
            return False
        return True