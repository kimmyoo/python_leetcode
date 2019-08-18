class Solution(object):
    #my own solution. learn other people's succinct solution
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        res = []
        l = len(S)
        i = 0
        while i < l-1:
            start, end = i, i
            while S[i] == S[i+1]:
                end = i+1
                i+=1
                # remember to check if i reaching to the last char
                if i == l-1:
                    break
            #check to see if large group has been found
            if end - start >=2:
                res.append([start, end])
            #check to see if single char has been found, 
            #if found, increment both start and end pointers
            if start == end:
                i+=1
        return res


s = Solution()
S = "abcdddeeeeaabbbcd"
res = s.largeGroupPositions(S)
print(res)