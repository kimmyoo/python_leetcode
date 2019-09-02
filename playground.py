class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        #my own solution. check out stack implementation
        def transformToList(string):
            #counter is used to remember how many "#" has been met
            temp, counter = [], 0
            i = len(string) -1 
            while i >= 0:
                if string[i] != "#":
                    #only when we have no "#" encountered, we append the char to temp
                    if counter == 0:
                        temp.append(string[i])
                    #if the counter is not 0, only update the counter
                    else:
                        counter-=1
                else:
                    counter += 1
                i-=1
            return temp
        
        sList= transformToList(S)
        tList = transformToList(T)
        return sList== tList

s = Solution()
S = "ab#c"
T = "ad#c"
res = s.backspaceCompare(S, T)
print(res)
