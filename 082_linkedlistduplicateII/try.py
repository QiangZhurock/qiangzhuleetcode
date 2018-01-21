# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
"""
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #also note that the duplicates appear consequtively in a sorted list
        #since the "if" which deals with first node use head.next, here we also need to judge head.next
        if head is None or head.next is None:
            return head
        
        dummy = ListNode(0)
        rear = dummy
        #dummy.next = head
        
        #first node
        if head.val != head.next.val:
            rear.next = head
            rear = head
        head_pre = head
        head = head.next
        
        #middle node
        while head and head.next:
            if head.val != head.next.val and head_pre.val != head.val:
                rear.next = head
                rear = head
            head_pre = head
            head = head.next
            
        #last node
        if head.next is None and head_pre.val != head.val:
            rear.next = head
            rear = head
        
        rear.next = None
        return dummy.next
            
        