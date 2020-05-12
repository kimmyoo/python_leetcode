class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        refer to: merge intervals
        """
        temp = []
        ans = []
        
        A.extend(B)
        #sort the interval 
        A.sort(key = lambda x:x[0])
        
        for interval in A:
            if not temp:
                temp.append(interval)
            else:
                pre = temp[-1]
                if interval[0] > pre[1]:
                    temp[-1] = interval
                    continue
                intersection = [max(pre[0], interval[0]), min(pre[1], interval[1])]
                ans.append(intersection)
                #this line checks if we really need to replace the last interval in temp
                #if the right end is greater than the previous interval right end, we replace 
                if interval[1] >= pre[1]:
                    temp[-1] = interval
        return ans