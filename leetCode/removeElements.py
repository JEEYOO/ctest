def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        loop = ListNode() #Optional[ListNode]
        answer = loop
        while head  : #None
            if head.val != val :
                loop.next = ListNode(head.val)
                loop = loop.next
            head = head.next    

        return answer.next
