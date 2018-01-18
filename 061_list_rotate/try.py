# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
Given a list, rotate the list to the right by k places, where k is non-negative.
For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
"""
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        #get the length
        dummy = head
        length = 0
        while dummy:
            length += 1
            dummy = dummy.next
        
        #deal with special cases   
        if k >= length and length != 0:
            k = k % length
        if k == 0 or length == 1 or length == 0:
            return head
        
        #find the position
        rightlist = ListNode(0)
        p = head
        q = head
        count = 0
        while length - count > k:
            count += 1
            q = p
            p = p.next
        
        rightlist.next = p
        q.next = None
        #make the right part of the original list to be the left part of the new rotated list.
        """
        Given 1->2->3->4->5->NULL and k = 2,

        return 4->5->1->2->3->NULL.
        just like move 4->5 to the left
        """
        result = rightlist.next
        pre = rightlist.next
        while rightlist is not None:
            pre = rightlist
            rightlist = rightlist.next
        pre.next = head
        return result
        
        
        