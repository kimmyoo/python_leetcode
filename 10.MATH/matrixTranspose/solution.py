class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """

        l = len(A[0])
        B = []
        for i in range(l):
            B.append([l[i] for l in A])  
        return B

#test code
s = Solution()
#input cannot be [1, 2, 3]
A = [[1], [2], [3]]
B = s.transpose(A)
print(B)
