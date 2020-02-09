class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.accu = [0]
        for num in nums: 
            #the last item in nums is always the sum upto current index
            print (self.accu[-1])
            self.accu.append(self.accu[-1] + num)

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int 
        :type j: int
        :rtype: int 
        """
        #the range is from i to j   so sum up to j + 1 - sum up to i 
        #is the result
        return self.accu[j + 1] - self.accu[i]
        

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)