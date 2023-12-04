class Solution:
    def largestGoodInteger(self, num: str) -> str:
        left, right = 0, 1
        curNum = -1
        while (right < len(num)):
            curCount = 1
            while num[left]!=num[right] and right < len(num)-1:
                left+=1
                right+=1

            # if seeing equal pairs
            while(num[left] == num[right] and right < len(num)):
                curCount += 1
                if curCount == 3:
                    curNum = max(curNum, int(num[right]))
                if right == len(num)-1:
                    if curCount==3:
                        curNum = max(curNum, int(num[right]))
                    break
                right += 1
            right += 1
            left = right-1
        
        return "" if curNum < 0 else str(curNum) *3


s = Solution()
res = s.largestGoodInteger("1319300001111178371877777")
print(res)

