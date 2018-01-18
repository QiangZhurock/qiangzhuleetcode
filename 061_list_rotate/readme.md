0. """
        Given 1->2->3->4->5->NULL and k = 2,

        return 4->5->1->2->3->NULL.
        just like move 4->5 to the left
   """
1. Recalling the problems about rotated array, this description is misleading. For those who have trouble understanding this problem like me, think of the SLL as a circle.
2. error:
 Last executed input:
[]
1
Line 31: q.next = None, AttributeError: 'NoneType' object has no attribute 'next'
3. error 
TLE: 
Last executed input:
[1]
1
4. TLE:
Last executed input:
[1,2]
2
5. TLE:

Last executed input:
[1,2]
3