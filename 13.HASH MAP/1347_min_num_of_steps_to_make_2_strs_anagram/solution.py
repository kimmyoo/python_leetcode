class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        #Letters those only appear in T
        #Letters those appear in T more than S with the difference as value
        #                              “leetcode”
        #                              "practice"
        #diff of counterT and count S:  111101 
        extra = 0
        counterS = collections.Counter(s)
        counterT = collections.Counter(t)
        for k in counterT:
            if k in counterS:
                if counterT[k] >= counterS[k]:
                    extra += counterT[k] - counterS[k]
            else:
                extra += counterT[k] - counterS[k] # here counterS[k] is 0
        return extra
