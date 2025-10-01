def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        resultList = [] 

        resultList = self.addPreOrderVal(root,resultList)

        return resultList
    
    def addPreOrderVal(self, root: Optional[TreeNode], rList: List[int]) -> List[int]:
        if root is None : return rList

        rList.append(root.val)
        self.addPreOrderVal(root.left, rList)
        self.addPreOrderVal(root.right, rList)

        return rList
