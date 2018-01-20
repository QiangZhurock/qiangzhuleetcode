# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        length = 0
        dummy = root
        while dummy:
            length += 1
            dummy = dummy.next
        width, remainder = divmod(length, k)
        # print width, remainder
        result = []
        result.append
        # for i in xrange(0, part_number):
        # result.append(ListNode(""))
        part_count = 0

        cur = root
        for i in xrange(0, k):
            head = ListNode(0)
            rear = head
            # create each list part, loop parti_number times
            for j in xrange(0, width + (i < remainder)):
                # also works, remember rear.next = None
                rear.next = cur
                rear = cur

                # here is important
                # rear.next = ListNode(cur.val)
                # rear = rear.next

                # if cur:
                cur = cur.next
            # set rear.next to None
            rear.next = None
            result.append(head.next)

            # print root.val
        return result


if __name__=="__main__":
    lst = [ListNode(1), ListNode(2), ListNode(3), ListNode(4)]
    for ind in xrange(len(lst)-1):
        lst[ind].next = lst[ind+1]
    Solution().splitListToParts(lst[0], 5)
    #while head:
      #  print head.val
       # head =head.next