def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    
        #SELECT ONE(A|B) AND STORE IN IN A LIST 
        listA = []
        
        while headA is not None and headA.next is not None : 
            listA.append(headA.val)
            headA = headA.next 
        
        #USE 'IN' TO CHECK FOR THE OTHER LIST AND RETURN IF FOUND
        while headB is not None and headB.next is not None : 
            if headB.val in listA :
                return headB
            else : 
                headB = headB.next
        
        return None
