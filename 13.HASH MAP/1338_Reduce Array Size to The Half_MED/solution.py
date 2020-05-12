class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        half = len(arr)/2
        d = collections.Counter(arr)
        c = d.values()
        c.sort(reverse=True)

        if max(c) >= half:
            return 1
        begin, end = 0, 1
        sum = max(c)
        
        while True:
            sum += c[end]
            if sum >= half:
                return end+1-begin
            else:
                end+=1
