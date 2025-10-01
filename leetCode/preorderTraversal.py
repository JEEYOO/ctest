def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        resultList = [] 

        def addPreOrderVal(root: Optional[TreeNode], rList: List[int]) -> List[int]:
            if root is None : return rList

            rList.append(root.val)
            addPreOrderVal(root.left, rList)
            addPreOrderVal(root.right, rList)

            return rList

        resultList = addPreOrderVal(root,resultList)

        return resultList
