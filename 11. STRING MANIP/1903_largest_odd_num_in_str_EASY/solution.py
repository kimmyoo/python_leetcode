class Solution:
    def largestOddNumber(self, num: str) -> str:
        i = len(num)-1
        while int(num[i]) % 2 == 0 and i>0:
            i-=1

        if i==0 and int(num[i])%2 == 0:
            return ""
        return num[0:i+1]