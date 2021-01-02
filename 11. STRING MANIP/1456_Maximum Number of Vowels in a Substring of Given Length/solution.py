class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        credits to: lee215
        """
        # sliding window problem, 
        # use 0 or 1 to represent if a char in current substring
        # use substract and addition a varaible cur to represent incoming or leaving of a vowl.
        res = cur = 0
        l = len(s)
        for i in xrange(l):
            # cur += 0 or 1
            cur += s[i] in 'aeiou'
            # for first 3 chars, only update cur by looking at the current incoming chars 
            # after i >= k, the sliding window starts to leave the beginning, so need to subtract whether the leaving char from the beginning is in "aeiou"
            if i >= k:
                cur -= s[i-k] in 'aeiou'
            res = max(cur, res)
        return res