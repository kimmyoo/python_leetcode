class Solution():
    def multiply (self, str1, str2):
        len1 = len(str1)
        len2 = len(str2)
        # reverse the strings for loop multiplication
        str1 = str1[::-1]
        str2 = str2[::-1]
        temp = [ 0 for n in range (len1 + len2)]
        
        for i in range (len1):
            for j in range (len2):
                temp[i + j] += int(str1[i]) * int(str2[j])
        
        carry = 0
        res_str = []
        
        for num in temp:
            digit = carry + num
            carry = digit // 10
            digit = digit % 10
            res_str.append(str(digit))
        
        # use string join() to joint the digits
        res_str = "".join(res_str[::-1])
        
        # get rid of preceding 0s. 
        index = 0
        # -1 ensure the scenario result is 0
        for i in range (len1 + len2 -1):
            if res_str[i] == '0':
                index += 1
            else:
                break
        res_str = res_str[index:]
        return res_str
        

s = Solution()
res = s.multiply('3', '1111')
print (res)

        
