class Solution(object):
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        l1length = self.length(l1)
        l2length = self.length(l2)

        l1n = 0
        l2n = 0

        l1copy = l1
        l2copy = l2

        for i in range(l1length) : 
            l1n += l1copy.val * (10 ** i)
            l1copy = l1copy.next
        #print(l1n)
        for i in range(l2length) : 
            l2n += l2copy.val * (10 ** i)
            l2copy = l2copy.next

        answerNum = l1n + l2n
        #print(answerNum)
        #최종값만 reverse로

        reverseAnswer = list(str(answerNum))
        #answer = [8,0,7]
        #print(reverseAnswer[0])
        answer = ListNode(int(reverseAnswer[-1]))
        current = answer

        for i in range(len(reverseAnswer)-2, -1, -1):
            current.next = ListNode(int(reverseAnswer[i]))
            current = current.next
        #self.print_list_node(current) 8
        self.print_list_node(answer) 
        
        return answer.next
    
    def length(self, whatever:ListNode) -> int:
        lengthNum = 0
        while whatever:
            lengthNum += 1
            whatever = whatever.next
        return lengthNum

    def print_list_node(self, head: ListNode) -> None:
        current = head
        while current:
            print(current.val, end=" -> " if current.next else "")
            current = current.next
        print()  # change line             
