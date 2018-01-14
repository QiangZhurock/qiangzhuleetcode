"""
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
Example:
Given a = 1 and b = 2, return 3.
"""

__author__ = 'Daniel'


class Solution(object):
    def getSum(self, a, b):
        """
        circuit full-adder
        since Python don't restrict to 32bit, we need
         1. Masking
         2. Overflow handling
        :type a: int
        :type b: int
        :rtype: int
        """
        # >>  move right
        # <<  move left
        # |   bit or
        # &   bit and
        # ^   bit nor
        # ~   versa
        MAX = 0x7FFFFFFF
        MSK = 0xFFFFFFFF
        numtest = 0x7F
        bitand = a & b
        moverleft = 10 << 1
        carry = (a & b) << 1
        out = a ^ b

        # convert to 32 bit
        carry &= MSK
        out &= MSK

        if carry != 0:
            return self.getSum(out, carry)
        else:
            # handle overflow
            if out < MAX:
                return out
            else:  # negative
                return ~(out ^ MSK)

if __name__ == "__main__":
    print Solution().getSum(7,7)