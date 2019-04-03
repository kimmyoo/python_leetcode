"""
Given an array A of non-negative integers, return an array consisting 
of all the even elements of A, followed by all the odd elements of A.
You may return any answer array that satisfies this condition.
Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
"""

class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        n = len(A)
        i = 0
        j = n-1
        
        while i < j:
            #A[i] is even
            if A[i] & 1 == 0:
                #A[j] is odd
                if A[j] & 1 != 0:
                    i+=1
                    j-=1
                #A[j] is even
                else:
                    i+=1
            #A[i] is odd
            else:
                # A[j] is odd
                if A[j] & 1 != 0:
                    j-=1
                # A[j] is even
                else:
                    A[i], A[j] = A[j], A[i]
                    i+=1
                    j-=1
        return A

#test
s = Solution()
A = [1, 3, 5, 7, 8, 11, 2, 6, 77]
B = s.sortArrayByParity(A)
print(B)




#~ # leet code solution
#~ class Solution(object):
    #~ def sortArrayByParity(self, A):
        #~ if not A:
            #~ return A
        
        #~ start = 0
        #~ for i in range(len(A)):
            #~ if A[i] % 2 == 0:
                #~ A[i], A[start] = A[start], A[i]
                #~ start += 1
        #~ return A
