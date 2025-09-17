class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if root is None :
            return False
        elif targetSum == root.val and root.left is None and root.right is None :
            return True
        
        newTarget = targetSum - root.val    

        leftval = self.calSum(root.left)
        rightval = self.calSum(root.right)

        result1 = result + leftval
        result2 = result + rightval 

        #print(result1)

        if newTarget == leftval and root.left is None and root.right is None :
            return True
        elif newTarget == rightval and root.left is None and root.right is None :
            return True
        else : return self.hasPathSum(root.left, newTarget) or self.hasPathSum(root.right, newTarget)

    def calSum(self, root: Optional[TreeNode]) -> int:
        if root is None :
            return 0
        
        return root.val

'''
if rightval == result or leftval == result:
            return True
        else : return False
'''
