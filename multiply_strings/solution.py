#
# Given two numbers represented as strings, return multiplication of the numbers as a string.
# 
# Note: The numbers can be arbitrarily large and are non-negative.
#
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        #reverse a string 
        num1 = num1[::-1]
        num2 = num2[::-1]
        length1 = len(num1)
        length2 = len(num2)
        # the # of digits of the multiplication result is at most len 1+len 2
        # initiate a list of 0s with a length of len1 + len2
        temp = [0 for n in range(length1 + length2)]
        # Do multiply, really nned to look at a picture to understand
        for i in range(length1):
            for j in range(length2):
                temp[i + j] += int(num1[i]) * int(num2[j])
        
        carry = 0
        digits = []
        # Do plus
        for num in temp:
            s = carry + num
            carry = s // 10 # floor division to get carry 
            digits.append(str(s % 10)) # modulo to get digit 
        
        #reverse the string again
        result = "".join(digits)[::-1]
        
        # Remove the surplus zero
        sub_index = 0
        for i in range(length1 + length2 - 1):
            if result[i] == "0":
                sub_index += 1
            else:
                break
        result = result[sub_index:]
        return result

if __name__ == "__main__":
    s = Solution()
    assert s.multiply("120", "20000") == "2400000"
    assert s.multiply("0", "3421") == "0"
    print (s.multiply("1111111", "9"))
    
