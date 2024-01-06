from typing import Optional
from treeSetup import TreeNode

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        """
        :type t: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        if not root.left and not root.right:
            return str(root.val)
        if not root.right:
            return str(root.val) + '(' + self.tree2str(root.left) + ')'
        return str(root.val) + '(' + self.tree2str(root.left) + ')('+ self.tree2str(root.right) + ')'


    def tree2strVII(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(root, res):
            if not root:
                return
            res.append(str(root.val))

            # first left
            if root.left:
                res.append("(")
                dfs(root.left, res)
                res.append(")")
            # when dealing with right 
            # remember to add () first
            if root.right and not root.left:
                res.append("()")
            
            if root.right:
                res.append("(")
                dfs(root.right, res)
                res.append(")")
        
        dfs(root, res)
        return "".join(res)