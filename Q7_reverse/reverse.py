class Solution(object):
    #deal with reversed integer overflows, return 0, what is the limit of overflowing.
    #also, should deal with 123->321, 120->21, -123->-321
    def reverse(self, x):

        if(x < 0):
            sign = -1
            x = abs(x)
        else:
            sign = 1
        strx = str(x) #produce a printable string representation
        lst = list(strx)
        lst.reverse()
        y = ''.join(lst) # '021'
        x = ''.join(lst)

        print x #021
        x = int(x)
        result = sign * x
        #print lst
        #print lst
        #print 0x7F
        if abs(result) > 0x7FFFFFFF: #16 jinzhi,F is 15
            return 0
        else:
            return result


if __name__ == "__main__":
    x = 120
    print Solution().reverse(x)