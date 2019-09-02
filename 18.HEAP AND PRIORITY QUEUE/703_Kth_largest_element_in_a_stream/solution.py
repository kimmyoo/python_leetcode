import heapq
class KthLargest(object):
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.heap = nums
        print(self.heap)
        heapq.heapify(self.heap)
        print(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)
        
    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        #this is for case where there is less than k elements in heap
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        #need to push then pop the smallest element
        else:
            heapq.heappushpop(self.heap, val)
        return self.heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
k = 3
nums = [4,5,8,2]
s = KthLargest(k, nums)
res1 = s.add(9)
res2 = s.add(0)
res3 = s.add(100)
print(res1, res2, res3)

"""
q = []
heappush(q, item)
heappop(q) # pop最小的出来, 如果只return最小的不pop出来，则用q[0]即可
heappushpop(q, item) # 先push再pop
heapify(q) # Transform list x into a heap, in-place, in linear time.
heapreplace(q, item) #先pop再push
nlargest(n, q) # return 前 n个最大的数作为list
"""