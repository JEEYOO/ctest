class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        
        result = []
        
        def traverse(node):
            if node is None:
                return
            traverse(node.left) #Far left
            result.append(node.val)
            traverse(node.right)

        traverse(root)
        
        return result
