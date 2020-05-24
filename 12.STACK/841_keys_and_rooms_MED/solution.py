class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        unused = [0]
        #set() takes an iterable so instead of var = set(0), do SET.add()
        seen = set(unused)
        
        while unused:
            cur = unused.pop()
            for key in rooms[cur]:
                if key not in seen:
                    seen.add(key)
                    unused.append(key)
                    #this line can make the code fast for some cases
                    if len(seen) == len(rooms): return True
        return len(seen) == len(rooms)
