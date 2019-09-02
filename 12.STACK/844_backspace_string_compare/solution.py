"""
Given two strings S and T, return if they are equal when both are typed into empty text editors. 
# means a backspace character.
Example:
Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
"""
class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        #my own solution: transform the string into list in reversed order
        #when you see a '#' update counter to remember how many "#" has been met
        #ignore corresponding times of char in reverse order. 
        #then compare two transformed lists
        # check out stack implementation! and how to implement in o(1) space and o(n) time
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
