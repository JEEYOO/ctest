# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        answer : Optional[ListNode] = ListNode(0)
        answer2 = answer

        while list1 and list2 :
            if list1.val < list2.val :
                answer.next = ListNode(list1.val)
                answer = answer.next
                list1 = list1.next
                
            else :
                answer.next = ListNode(list2.val)
                answer = answer.next
                list2 = list2.next
        
        if list1 is None:
            while list2 :
                answer.next = ListNode(list2.val)
                answer = answer.next
                list2 = list2.next

        if list2 is None:
            while list1 :
                answer.next = ListNode(list1.val)
                answer = answer.next
                list1 = list1.next
        
        return answer2.next
        
        #return list1
    
    

"""
while self.leng(answer) != self.leng(list1)+self.leng(list2) :

#last node
while list1.next:
    list1 = list1.next
"""
