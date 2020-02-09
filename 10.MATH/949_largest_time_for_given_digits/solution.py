class Solution(object):
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        #knowledge point permutations() in itertools 
        pList = sorted(list(itertools.permutations(A)), reverse = True)
        #print(pList)
        
        for p in pList:
            a, b , c, d = p
            hr = a*10 + b
            mi = c*10 + d
            if hr < 24 and mi < 60:
                return "{}{}:{}{}".format(a, b, c, d)
        return ""
