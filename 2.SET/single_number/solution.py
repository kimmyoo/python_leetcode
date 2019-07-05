class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set1 = set()
        set2 = set()
        # first round
        # adding unique ele into set
        # then remove unique elements(rest in list are repeating elements)
        for ele in nums:
            if ele not in set1:
                set1.add(ele)
            else:
                set2.add(ele)
        res = set1 - set2
        return res.pop()

    # leetcode solution, hash table 没看
    """
    We use hash table to avoid the O(n) time required for searching the elements.  
    1. Iterate through all elements in  nums nums 
    2. Try if  hash_table has the key for pop 
    3. If not, set up key/value pair 
    4. In the end, there is only one element in hash_table, so use popitem to get it
    """
    def singleNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_table = {}
        for i in nums:
            try:
                hash_table.pop(i)
            except:
                hash_table[i] = 1
        return hash_table.popitem()[0]
#test code
s = Solution()
testList = [1,0,1]
res = s.singleNumber(testList)
print(res)
