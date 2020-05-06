class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        opening, count = 0, 0
        for ch in S:
            if ch == "(":
                opening += 1
            else:
                if opening > 0:
                    opening -=1
                else:
                    count +=1
        return count + opening

    def minAddToMakeValid2(self, S):
        """
        :type S: str
        :rtype: int
        """
        dq = collections.deque()
        l = []
        stackEmpty = True
        for ch in S:
            if ch == ")":
                if len(dq) == 0:
                    l.append(ch)
                    stackEmpty = False
                else:
                    dq.pop()
                    if len(dq) == 0:
                        stackEmpty = True
            else:
                dq.append(ch)
                stackEmpty = False
        if not stackEmpty:
            return len(l) + len(dq)
        else: return max(len(l), len(dq))