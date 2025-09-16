class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None :
            return 0
        
        left = self.minDepth(root.left)    
        right = self.minDepth(root.right)

        if root.left is None :
            return right + 1
        elif root.right is None :
            return left + 1
        else: 
            return min(left,right) +1
