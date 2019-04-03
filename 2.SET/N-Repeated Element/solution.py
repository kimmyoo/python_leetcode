class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        temp = []
        for ele in A:
            if ele not in temp:
                temp+=[ele]
            else:
                return ele


#test
s = Solution()
A = [5,1,5,2,5,3,5,4]
B = s.repeatedNTimes(A)
print(B)
