def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    
        #SELECT ONE(A|B) AND STORE IN IN A LIST 
        listA = []
        
        while headA is not None : #and headA.next is not None 
            listA.append(headA)
            headA = headA.next 
        
        #USE 'IN' TO CHECK FOR THE OTHER LIST AND RETURN IF FOUND
        while headB is not None : 
            if headB in listA :
                return headB
            headB = headB.next
        
        return None
