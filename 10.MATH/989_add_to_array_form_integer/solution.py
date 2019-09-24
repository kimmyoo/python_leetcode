class Solution(object):
    #my solution
    #the trick is to use the K as the carry at the beginning
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        l = len(A)
        carry = K
        newCarry = 0
        #this loop is dealing with lower end of the sum
        #use a variable newCarry to remember the carry before changing A[l-i-1]
        #sum carry and original element and use mod operation to find the digit of the sum
        #update carry
        for i in range(l):
            newCarry = (A[l-i-1] + carry) // 10
            A[l-i-1] = (A[l-i-1] + carry) % 10
            carry = newCarry
        #use the remaining carry to find the rest of the digits and insert 
        #the digit from the beginning of the list one at a time
        while carry > 0:
            digit = carry % 10
            A.insert(0, digit)
            carry = carry // 10
        return A
s = Solution()
A = [9,9,9,9,9,9,9,9,9,9]
K = 1
res = s.addToArrayForm(A, K)
print(res)