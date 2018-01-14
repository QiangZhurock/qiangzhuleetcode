class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # 32 bits interger max
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        MIN = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        while(b != 0):
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask

        # if a is negative, get a's 32 bits complement positive first
        # then get 32-bit positive's Python complement negative

        # >>  move right
        # <<  move left
        # |   bit or
        # &   bit and
        # ^   bit nor
        # ~   versa

        return a if a <= MAX else ~(a ^ mask)

    def getSum2(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        MIN = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        #&test
        test = 8 & 3
        while b != 0:
            # ^ get different bits and & gets double 1s, << moves carry
            bitand = a & b
            #moverleft = 10 << 1
            carry = (a & b) << 1
            out = a ^ b
            #convert to 32 bit
            a, b = out & mask, carry & mask
        # if a is negative, get a's 32 bits complement positive first
        # then get 32-bit positive's Python complement negative
        return a if a <= MAX else ~(a ^ mask)

if __name__ == "__main__":
    print Solution().getSum2(7,7)