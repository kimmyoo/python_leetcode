class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        print(arr)
        l = len(arr)
        i = 0
        while i < l-1:
            #if the current element is 0, 
            #move the rest one position to right starting from 
            #the last element
            if arr[i] == 0:
                for j in range(l-2, i,-1):
                    arr[j+1] = arr[j]
                arr[i+1] = 0
                i+=2
            else:
                i+=1
        return

#my method is NOT the best, take a look at the leetcode solution!
s = Solution()
testArr = [1, 0, 0, 9, 0, 1, 6, 6, 4,0]
s.duplicateZeros(testArr)
print(testArr)
