# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool: 
        if p is None and q is None : return True
        elif p is None or q is None : return False
        elif p.val != q.val : return False

        temp_left = self.isSameTree(p.left, q.left)
        temp_right = self.isSameTree(p.right, q.right)

        return temp_left and temp_right
'''
elif : return isSameTree(self, p.left, q.left) and isSameTree(self, p.right, q.right)
        else : return False 

if p == q : return True 
else : return False
''' 
        
