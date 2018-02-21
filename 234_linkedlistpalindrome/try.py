# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
Given a singly linked list, determine if it is a palindrome.
Follow up:
Could you do it in O(n) time and O(1) space?
"""
class Solution(object):
    def isPalindrome_version1(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        if head is None:
            return True
        reversed_list = self.reverseList(head)
        while head is not None:
            if head.val != reversed_list.val:
                return False
            head = head.next
            reversed_list = reversed_list.next
        return True

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        
        Algorithms:
        1. put into array O(N)
        2. midpoint, reverse the other - O(n) time and O(1) space
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return True
        
        length = self.len(head)
        
        #find mid_index, like 1-2-3-2-1, 5/2 = 2, need to reverse 2-1.
        mid_index = length / 2
        if length % 2 != 0:
            mid_index += 1
            
        #find mid node
        mid_node = self.get_midnode(head, mid_index)
        
        #reverse the list after mid_point
        reversed_list = self.reverseList(mid_node)
        while head and reversed_list:
            if head.val != reversed_list.val:
                return False
            head = head.next
            reversed_list = reversed_list.next
        return True
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
    
    def len(self, head):
        length = 0
        while head is not None:
            length += 1
            head = head.next
        return length
    def get_midnode(self, head, index):
        count = 0
        while count < index:
            count += 1
            head = head.next
        return head
        

    def isPalindrome1(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        result = []
        while(head is not None):
            result.append(head.val)
            head = head.next
        return result == result[::-1]
        