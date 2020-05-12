class Solution(object):
    def pancakeSorting(self, A):
        """
        找到最大的数字，假设它的下标是i
        反转0到i之间的数字，使得A[i]变成第一个数
        反转整个数组，让最大的数到末尾
        """
        l = len(A)
        res = []
        for i in range(l):
            curMax = max(A[:l-i])
            n = 0
            while A[n] != curMax:
                n+=1
            #need to include the curMax
            A[:n+1] = reversed(A[:n+1])
            res.append(n+1)
            A[:l-i] = reversed(A[:l-i])
            res.append(l-i)
        return res
    

s = Solution()
A = [3,2,4,1]
print(s.pancakeSorting(A))