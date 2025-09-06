class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root.left is None and root.right is None : 
            return self.isMirror(root.left, root.right)
        elif root.left is None or root.right is None : return False
        else : return self.isMirror(root.left, root.right)

    def isMirror(self, rootL: Optional[TreeNode], rootR: Optional[TreeNode]) -> bool:   
        if rootL is None and rootR is None : return True
        elif rootL is None or rootR is None : return False
        elif rootL.val == rootR.val : return self.isMirror(rootL.left, rootR.right) and self.isMirror(rootL.right, rootR.left)
        else : return False
