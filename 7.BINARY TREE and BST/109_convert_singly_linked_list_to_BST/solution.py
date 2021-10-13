# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        sortedArray = []
        while head:
            sortedArray.append(head.val)
            head = head.next
        
        def helper(left, right):
            if left > right:
                return None
            mid = (left + right)//2
            root = TreeNode(sortedArray[mid])
            root.left = helper(left, mid-1)
            root.right = helper(mid+1, right)
            return root
        res = helper(0, len(sortedArray)-1)
        
        return res