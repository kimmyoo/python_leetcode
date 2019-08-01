class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        Follow up:
        Could you do it without any loop/recursion in O(1) runtime?
        """
        
        """
        from:
        class Solution(object):
            def addDigits(self, num):
                intNum = [int(i) for i in str(num)]
                print (intNum)
                total = sum(intNum)
                l = len(intNum)
                if l==1:
                    return total
                else:
                    return self.addDigits(total)
        to:
        """
        
        intNum = [int(i) for i in str(num)]
        print (intNum)
        s = sum(intNum)
        return s if len(intNum) == 1 else self.addDigits(s)


#test code
s = Solution()
num =  1234
sum = s.addDigits(num)
print(sum)
