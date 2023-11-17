class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = {}
        numOfDel = 0

        for ch in s:
            if ch not in m:
                m[ch] = 1
            else:
                m[ch] += 1
        
        # list of tuple pairs in non-increasing order 
        sortedTuples= sorted(m.items(), key=lambda item: item[1], reverse=True)
        
        m = {}
        
        for tpl in sortedTuples:
            if tpl[1] not in m.values():
                m[tpl[0]] = tpl[1]
            else:
                temp = tpl[1]
                if temp == 1:
                    numOfDel += 1
                else:
                    while temp in m.values():
                        temp -= 1
                        numOfDel += 1
                    # tricky part is here
                    if temp == 0:
                        continue
                    m[tpl[0]] = temp
                
        return numOfDel


s = Solution()

str1 = "bbbbcea"
str2 = "beaddedbacdcd"
str3 = "ceabaacb"

res1 = s.minDeletions(str1)
res2 = s.minDeletions(str2)
res3 = s.minDeletions(str3)

print(res1, res2, res3)