# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        #int l1n, l2n
        print(l1)
        #print(l1.next)
        """
        length = l1.next
        for i in range(length):
             l2n += l2[length-i] * (10 ** (length - i))
             l1n += l1[length-i] * (10 ** (length - i))

        resultn = l1n + l2n 
        """

        #Divide and allocate to [ ]
