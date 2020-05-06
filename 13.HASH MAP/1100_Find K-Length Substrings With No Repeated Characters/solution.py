"""Given a string S, return the number of substrings of length K with no repeated characters.

Example 1:
Input: S = "havefunonleetcode", K = 5
Output: 6
Explanation: 
There are 6 substrings they are : 'havef','avefu','vefun','efuno','etcod','tcode'.

Example 2:
Input: S = "home", K = 5
Output: 0
"""
class Solution(object):
    def numKLenSubstrNoRepeats(self, S, K):
        l = len(S)
        res = 0
        if K > l:
            return 0
        
        m  = {}
        #put first K ch in hashmap
        for i in range(K):
            if S[i] not in m:
                m[S[i]] = 1
            else:
                m[S[i]]+=1
        #check the first substring
        if self.isUnique(m): res +=1
        print(S[0:K])
        
        #put in the rest and check
        for i in range(K, l):
            chIn = S[i]
            chOut = S[i-K]
            if chIn not in m:
                m[chIn] = 1
            else:
                m[chIn] += 1
            m[chOut] -= 1
            if self.isUnique(m):
                res +=1
                print(S[i-K+1:i+1])
        return res
            
    def isUnique(self, m):
        for k in m:
            if m[k] >= 2:
                return False
        return True

s = Solution()
S = "havefunonleetcode"
K = 6
ans = s.numKLenSubstrNoRepeats(S, K)
print(ans)
    