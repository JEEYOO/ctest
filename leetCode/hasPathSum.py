class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if root is None :
            return False

        result = root.val    

        leftval = self.calSum(root.left)
        rightval = self.calSum(root.right)

        result1 = result + leftval
        result2 = result + rightval 

        #print(result1)

        if targetSum == result1:
            return True
        else : return False

    def calSum(self, root: Optional[TreeNode]) -> int:
        if root is None :
            return 0
        
        return root.val

'''
if rightval == result or leftval == result:
            return True
        else : return False
'''
