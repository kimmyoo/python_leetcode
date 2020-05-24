"""
solution to to_lowercase
"""
class Solution():
    """
    solution to to_lowercase
    """
    def to_lower_case(self, str):
        """
        :type str: str
        :rtype: str
        """
        #return str.lower()
        str_list = [ord(letter) for letter in str]
        res = ''
        for letter in str_list:
            if 65 <= letter <= 90:
                letter += 32
                res += chr(letter)
            else:
                res += chr(letter)
        return res

s = Solution()
lowered = s.to_lower_case("Bull$hit")
print(lowered)
