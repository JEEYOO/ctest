# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        listVer = []

        while head:
            if head.val not in listVer :
                listVer.append(head.val)
            head = head.next

        setVer = set(listVer)
        #print(setVer)
        forCopy = ListNode() #Optional[ListNode]
        iteration = forCopy 

        for each in sorted(setVer):
            iteration.next = ListNode(each)   
            iteration = iteration.next

        answer = forCopy.next

        return answer
