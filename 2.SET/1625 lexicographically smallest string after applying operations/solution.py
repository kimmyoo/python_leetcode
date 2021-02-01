class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        #add operation
        def add(s, a):
            new = ""
            for i in range(len(s)):
                if i % 2 != 0:
                    new += str(int(s[i]) + a)[-1]
                else:
                    new += s[i]
            return new
        
        #rotate operation
        def rotate(s, b):
            return s[len(s)-b:] +s[:len(s)-b]
        
        seen = set()
        need = list()
        need.append(s)
        
        while need:
            cur = need.pop()
            if cur not in seen:
                seen.add(cur)
                need.extend([add(cur, a), rotate(cur, b)])
        
        return min(seen)

obj = Solution()
s, a, b = "5525", 9, 2
res = obj.findLexSmallestString(s, a, b)
print(res)