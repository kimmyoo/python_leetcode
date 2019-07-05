class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sumA = sum(A)
        sumB = sum(B)
        diff = 0
        setB = set(B)
        
        if sumA == sumB:
            for e in A:
                if e in B:
                    return [e, e]
        elif sumA > sumB:
            diff = int((sumA-sumB)/2)
            for e in A:
                if e - diff in setB:
                    return [e, e-diff]
        else:
            diff = int((sumB-sumA)/2)
            for e in A:
                if e + diff in setB:
                    return [e, e+diff]


    #leetcode solution
    def fairCandySwap2(self, A, B):
        Sa, Sb = sum(A), sum(B)
        setB = set(B)
        for x in A:
            if x + (Sb - Sa) / 2 in setB:
                return [x, int(x + (Sb - Sa) / 2)]
#test code
s = Solution()
A = [1, 1]
B = [2, 2]
res = s.fairCandySwap(A, B)
ans = s.fairCandySwap2(A, B)

print (res, ans)
