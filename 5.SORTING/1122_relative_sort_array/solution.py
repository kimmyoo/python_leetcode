class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        #this is my own soltuion
        d = {k:val for val, k in enumerate(arr2)}
        left = []
        right = []
        numOfNon = 0
        for i in range(len(arr1)):
            if arr1[i] not in arr2:
                right.append(arr1[i])
            else:
                left.append(arr1[i])
        
        right.sort()
        #sort the left half
        for j in range(1, len(left)):
            while d[left[j]] < d[left[j-1]] and j >=1:
                left[j], left[j-1] = left[j-1], left[j]
                j-=1
        
        return left+right

#test code
s = Solution()
arr1, arr2 = [2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]
res = s.relativeSortArray(arr1, arr2)
print(res)