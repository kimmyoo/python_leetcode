class Solution(object):
    #my own solution, convert list into a string 
    #and split string with '1'
    #find the maxLen and compare with first and last in the string list
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        maxLen = 0
        seatStr = ''.join(map(str, seats))
        seatList = seatStr.split('1')
        for s in seatList:
            if len(s) > maxLen:
                maxLen = len(s)
        if (maxLen+1)/2 > max(len(seatList[0]), len(seatList[-1])):
            return (maxLen+1)/2
        return max(len(seatList[0]), len(seatList[-1]))
    
    def maxDistToClosestB(self, seats):
        #implement with two pointers
        pass

s = Solution()
seats = [0,0,0,0,1,0,0,0,0,1]
print(s.maxDistToClosest(seats))