class Solution(object):
    def romanToInt1(self, s):
        """
        :type s: str
        :rtype: int
        """
        revString = s[::-1]
        d = {'I': 1, 
             'V': 5,
             'X': 10, 
             'L': 50,
             'C': 100,
             'D': 500,
             'M': 1000}
        sum = 0
        i = 0
        while i < len(s) :
            if revString[i] == 'V' or revString[i] == 'X':
                try:
                    if revString[i+1] == 'I':
                        sum = sum + d[revString[i]] - d[revString[i+1]]
                        i+=1
                    else:
                        sum += d[revString[i]]
                except IndexError:
                    sum += d[revString[i]]
            elif revString[i] == 'L' or revString[i] == 'C':
                try:
                    if revString[i+1] == 'X':
                        sum = sum + d[revString[i]] - d[revString[i+1]]
                        i+=1
                    else:
                        sum += d[revString[i]]
                except IndexError:
                    sum += d[revString[i]]
            elif revString[i] == 'D' or revString[i] == 'M':
                try:
                    if revString[i+1] == 'C':
                        sum = sum + d[revString[i]] - d[revString[i+1]]
                        i+=1
                    else:
                        sum += d[revString[i]]
                except IndexError:
                    sum += d[revString[i]]
            else:
                sum += d[revString[i]]
            i+=1
        return sum
                
    # this is the right way to solve this problem
    def romanToInt2(self, s):
        roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        z = 0
        for i in range(0, len(s) - 1):
            if roman[s[i]] < roman[s[i+1]]:
                z -= roman[s[i]]
            else:
                z += roman[s[i]]
        return z + roman[s[-1]]
    
    # this is ingenious
    def romanToInt3(self, s: str) -> int:
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += translations[char]
        return number

