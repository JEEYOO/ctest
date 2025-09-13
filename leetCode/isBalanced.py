def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None :
            return True

        left_depth = self.depthCheckL(root.left) 
        right_depth = self.depthCheckR(root.right) 

        # print(left_depth,right_depth)

        if abs(left_depth - right_depth) <= 1 :
            return True
        else : return False

    def depthCheckL(self, root: Optional[TreeNode]) -> int:
        if root is None :
            return 0
        depthLL = self.depthCheckL(root.left) + 1
        depthLR = self.depthCheckL(root.right) + 1
        return max(depthLL, depthLR)

    def depthCheckR(self, root: Optional[TreeNode]) -> int:
        if root is None :
            return 0
        depthRL = self.depthCheckR(root.left) + 1
        depthRR = self.depthCheckR(root.right) + 1
        return max(depthRL, depthRR)
