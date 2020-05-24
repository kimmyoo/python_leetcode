from heapq import heapify, heappush, heappop 

class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        #my own solution. take a look at other ppl's solutions.
        #this is not optimal
        res = ""
        d = {}
        for idx, ch in enumerate(S):
            d[ch] = idx + 1
        
        h = []
        heapify(h)
        for ch in T:
            if ch in d:
                #definitely can push a tuple to heap, it will use the tuple[0] as the key to
                #insert to the heap
                heappush(h, (d[ch], ch))
            else:
                heappush(h, (0, ch))

        for i in range(len(h)):
            res+= heappop(h)[1]

        return res
        #build a minheap
        #when pushing to the heap, if a key not in d, its idx is set to 0
        #when we enumerate in S, need to increment all value by 1
        #build a min Heap, push all (ch, d[ch]) in heap
        #then pop() tuple off the heap and form the res