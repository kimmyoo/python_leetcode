class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        # it's building the pyramid level by level, in each level from left to right
        # not my own solution though but this solution is easy to understand.
        
        m = collections.defaultdict(list)
        for triple in allowed:
            m[triple[:2]].append(triple[-1])
        
        def dfs(bottom, above):
            # final base case:
            if len(bottom) == 2 and len(above) == 1: 
                return True
            
            # level base case:
            # the above level is finished, moving up one level
            if len(above) == len(bottom) - 1:
                return dfs(above, "")
            
            curIndex = len(above)
            curBase = bottom[curIndex:curIndex+2]
            
            if curBase in m:
                for ch in m[curBase]:
                    if dfs(bottom, above+ch):
                        return True
            return False
            
        return dfs(bottom, "")

