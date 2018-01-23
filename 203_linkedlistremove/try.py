# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return head
        # if head.val =

        dummy = ListNode(0)
        #dummy.next = head #error
        rear = dummy
        cur = head
        #print cur.val
        while head:
            a = head.val
            if head.val == val:
                head = head.next
            else:
                rear.next = head
                rear = head
                head = head.next

        rear.next = None
        return dummy.next

if __name__=="__main__":
    lst = [ListNode(2), ListNode(1)]
    for ind in xrange(len(lst)-1):
        lst[ind].next = lst[ind+1]
    head = Solution().removeElements(lst[0], 2)
    while head:
        b =head.val
        print head.val
        head =head.next
