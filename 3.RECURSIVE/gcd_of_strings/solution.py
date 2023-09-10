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


#   str1 str2 中选小的长度 倒着来 try 每一长度的 前缀
#   isValid helper function 用来查看 当前长度 能不能 把两个字符串的长度整除
#   不能 肯定不行； 如果能 还要看 是由几倍的 基底base string构成
#   所以需要得到倍数 
    def gcdOfStrings2(self, str1, str2):
        #  make sure str2 is longer, str1 is shorter
        len1, len2 = len(str1), len(str2)

        def isValid(k):
            if len1 % k or len2 % k:
                return False
            # 得到倍数
            i, j = len1//k, len2//k
            base = str1[:k]
            return str1 == base * i and str2 == base * j

            
        for i in range(min(len1, len2), 0, -1):
            if isValid(i):
                return str1[:i]
        
        return ""




#test code
s = Solution()
res = s.gcdOfStrings2("ace", "aceaceace")
print(res)
