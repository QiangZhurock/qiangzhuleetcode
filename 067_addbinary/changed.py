class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        a_len = len(a)
        b_len = len(b)
        c = []
        j = b_len-1
        carry = 0

        if a_len < b_len:
            return self.addBinary(b, a)

        for i in xrange(a_len-1, -1, -1):
            if (j >= 0):
                bit_sum = int(a[i]) + int(b[j]) + carry #after adding carry, set it to zero
                carry = 0
                if bit_sum >= 2:
                    c.append(bit_sum % 2)
                    carry = 1
                else:
                    c.append(bit_sum)
                j -= 1
            else:
                bit_sum = int(a[i]) + carry
                carry = 0
                if bit_sum >= 2:
                    c.append(bit_sum %2)
                    carry = 1
                else:
                    c.append(bit_sum)
        #if a_len == b_len and carry == 1:  # no carry = 1 will lead to 0+0=00
        #    c.append(carry)
        if carry == 1:  # no carry = 1 will lead to 0+0=00
            c.append(carry)
        c.reverse()
        return ''.join(str(n) for n in c)


if __name__ == "__main__":
    print Solution().addBinary("1111", "1111") #"10101"

