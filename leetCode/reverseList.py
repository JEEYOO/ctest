def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        copy = ListNode()
        answer = copy

        #copy2 = head

        tempList = list()
        while head:
            tempList.append(head.val)
            head = head.next

        #print(tempList)

        num = len(tempList)-1 #4
        while num >= 0:
            copy.next = ListNode(tempList[num]) 
            copy = copy.next
            num -= 1

        return answer.next
