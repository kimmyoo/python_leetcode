class Solution(object):
    #leetcode solution
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        
        def dfs(root1, root2):
            if root1 is None and root2 is None:
                return True
            if root1 is None or root2 is None:
                return False
            if root1.val != root2.val:
                return False
            return (dfs(root1.left, root2.left) and dfs(root1.right, root2.right)) or\
                    (dfs(root1.left, root2.right) and dfs(root1.right, root2.left))
        return dfs(root1, root2)

    #my own solution
    def flipEquiv2(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        #edge cases
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        
        container1 = [root1]
        container2 = [root2]
        
        while container1 and container2:
            if len(container1) != len(container2):return False
            count = len(container1)
            for i in range(count):
                cur1 = container1.pop()
                cur2 = container2.pop()
                #skip None nodes append left and right children in container
                if cur1.left:container1.append(cur1.left)
                if cur1.right:container1.append(cur1.right)
                if cur2.left:container2.append(cur2.left)
                if cur2.right:container2.append(cur2.right)
                #sort each nodes at each level according to value
                container1.sort(key=lambda node: node.val)
                container2.sort(key=lambda node: node.val)
                #compare val in each level 
                temp1 = [node.val for node in container1]
                temp2 = [node.val for node in container2]

                if temp1 != temp2:
                    return False
        return True