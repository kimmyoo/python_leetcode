class Solution:
    def totalMoney(self, n: int) -> int:
        # 等差数列Arithmetic sequence
        # a1 + n*(n-1)*d/2  d is called common difference
        sum = 0
        weeks = n//7
        extraDays = n%7

        if extraDays:
            for i in range(extraDays):
                sum += (weeks+1) + i
        if weeks == 0:
            return sum
        else:
            sum += weeks*28
            sum += 0 + (weeks-1)*weeks*7//2
            return sum
        


s = Solution()
res=s.totalMoney(199)
print(res)