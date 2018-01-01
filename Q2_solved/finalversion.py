"""
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each
of their nodes contain a single digit. Add the two numbers and return it as a linked list.
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""


#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #to decide if we need to switch l1 and l2, make sure that we need l11 and l22
        #After switch, we only need to deal with one situation. An useful trick.
        l11_len = 0
        l22_len = 0
        l11 = ListNode(0)
        l22 = ListNode(0)
        l11 = l1
        l22 = l2
        while (l11 != None):
            l11_len += 1
            l11 = l11.next
        while (l22 != None):
            l22_len += 1
            l22 = l22.next
        l0 = ListNode(0)
        if l11_len < l22_len:
            l0 = l1
            l1 = l2
            l2 = l0
	   #addTwoNumbers(l2s[0],l1s[0])

        #some definitions
        l = ListNode(0)
        l.next = None
        rear = ListNode(0)
        rear = l
        flag = 0 #flag ==1 iff sum larger than 10

        while (l1 != None):
            p = ListNode(0)
            if (l2 != None):
                sum = l1.val + l2.val + flag
                if (sum < 10):
                    p.val = suM
                    flag = 0
                else:
                    p.val = sum - 10 #firstly wrote 0 by mistake
                    flag = 1
                l2 = l2.next
            else: #firstly wrote if by mistake, we should use else!!
                sum = l1.val + flag
                if (sum < 10):
                    p.val = sum
                    flag = 0
                else:
                    p.val = sum - 10
                    flag = 1
            # rear_insert the new node
            rear.next = p
            rear = p

            l1 = l1.next
        #deal with the situation that l1 and l2 have the same length, and the final sum is larger than 10
        if flag == 1:
            p = ListNode(1)
            #rear_insert
            rear.next = p
            rear = p

        #let final to be None
        rear.next = None
        #return, note that l = l.next since first value is zero
        l = l.next
        return l



if __name__ == "__main__":
    l1s = [ListNode(1), ListNode(4)]
    l2s = [ListNode(9), ListNode(9)]
    for i in range(len(l1s)-1):
        l1s[i].next = l1s[i+1]
    for i in range(len(l2s)-1):
        l2s[i].next = l2s[i+1]
    #head = ListNode(0)
    head = Solution().addTwoNumbers(l1s[0], l2s[0])
    #print head
    while (head != None):
        print head.val
        head = head.next