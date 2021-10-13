class TreeNode:
    def __init__(x):
        self.val = x
        self.right = None
        self.left = None

class Solution(object):
    def twoSumBSTs(self, root1, root2, target):
        ctner1, ctner2 = [], []
        self.collectToListInOrder(root1, ctner1)
        self.collectToListInOrder(root2, ctner2)
        
        l1, l2 = len(ctner1)-1, len(ctner2)-1
        ptr1, ptr2 = 0, l2
        
        while ptr1 < l1 and ptr2 > 0:
            s = ctner1[ptr1] + ctner2[ptr2]
            if s == target: return True
            elif s < target: ptr1+=1
            else: ptr2-=1
        return False
        
    def collectToListInOrder(self, root, container):
        if root:
            self.collectToListInOrder(root.left, container)
            container.append(root.val)
            self.collectToListInOrder(root.right, container)


            