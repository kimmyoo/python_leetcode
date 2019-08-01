class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        l1 = len(str1)
        l2 = len(str2)
        if l1 == l2:
            return str1 if str1 == str2 else ""
        else:
            if l1 < l2:
                str1, str2 = str2, str1
            # pay attention to here, we ALREADY swapped str1 and str2, we cannot use l1 and l2 
            # at the following slicing.
            if str1[:len(str2)] == str2:
                return self.gcdOfStrings(str1[len(str2):], str2)
            else:
                return ""


#test code
s = Solution()
res = s.gcdOfStrings("ace", "aceaceace")
print(res)
