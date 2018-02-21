# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #head insert
        dummy =ListNode(0)
        #head = head.next
        while head is not None:
            #print head.val
            p = ListNode(head.val)
            p.next = dummy.next
            dummy.next = p
            head = head.next
        return dummy.next