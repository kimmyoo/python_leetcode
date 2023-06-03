class Solution(object):
    def sortFromTail(self, l):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        l.sort(key=lambda x: x[-1], reverse=True)
        return l

s = Solution()
l = ["pen", "pencil", "peony", "pig"]
res = s.sortFromTail(l)
print(res)