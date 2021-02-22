from collections import deque

class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """

        # the trick is observe the relation between depth and stack[i]
        # for 'AB' format, the score of A is record by stack item. when score of B is calculated,
        # it will be updated to the previous same level scored by A 
        st = deque()
        st.append(0)
        
        for ch in S:
            if ch == "(":
                st.append(0)
                print(st)
            else:
                v = st.pop()
                if v == 0:
                    st[-1] += 1
                else:
                    st[-1] += 2*v
                print(st)
        return st.pop()