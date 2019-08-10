class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        #consider: bcdeabcdfa   to    bcdfabcdea
        numOfCorrect = 0
        if len(A)!=len(B):
            return False
        if len(A) == 0:
            return True

        for i in range(len(B)):
            if A[0] == B[i]:
                #pay attention to the boundaries
                for j in range(1, len(B)):
                    if A[j] == B[(i+j) % len(B)]:
                        numOfCorrect +=1
                        # len(A)-1
                        if numOfCorrect == len(A)-1:
                            return True
                    else:
                        numOfCorrect = 0
                        break
        return False

    def rotateString2(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        if len(A) == 0:
            return True
        for i in range(len(A)):
            if A[i:] + A[:i] == B:
                return True
        return False

    def rotateString3(self, A, B):
        return len(A) == len(B) and B in A+A



s = Solution()
A = "bbbacddceeb"
B = "ceebbbbacdd"
res = s.rotateString(A, B)
print(res)