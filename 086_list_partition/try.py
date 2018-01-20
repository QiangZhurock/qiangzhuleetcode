# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal
to x.
You should preserve the original relative order of the nodes in each of the two partitions.
For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
"""


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        # deal with special case
        if not head:
            return
        # head insert to smaller and larger, then link them.
        head_smaller = ListNode(0)
        rear_smaller = head_smaller
        head_larger = ListNode(0)
        rear_larger = head_larger
        #pre = head
        while head:
            #cur = head
            if head.val < x:
                rear_smaller.next = head
                rear_smaller = head
                #rear_smaller.next = None
            else:
                rear_larger.next = head
                rear_larger = head
                #rear_larger.next = None
            head = head.next

        rear_larger.next = None
        # concatenate 
        rear_smaller.next = head_larger.next


        head_larger1 = head_larger
        head_smaller1 = head_smaller

        #while head_smaller1:
         #   print head_smaller1.val
          #  head_smaller = head_smaller1.next
        #while head_larger1:
         #   print head_larger1.val
          #  head_smaller = head_larger1.next
        return head_smaller.next


if __name__=="__main__":
    lst = [ListNode(2), ListNode(1)]
    for ind in xrange(len(lst)-1):
        lst[ind].next = lst[ind+1]
    head = Solution().partition(lst[0], 1)
    while head:
        print head.val
        head =head.next