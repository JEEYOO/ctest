class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None :
            return True

        if self.depthCheck(root) == -1 :
            return False
        else : return False

    def depthCheck(self, root: Optional[TreeNode]) -> int:
        if root is None :
            return 0
        depthL = self.depthCheckL(root.left)
        depthR = self.depthCheckL(root.right)
        
        if depthL == -1 or depthR == -1 :
            return -1
        elif abs(depthL - depthR) > 1 :
            return -1
        else :
            return max(depthLL, depthLR) + 1
