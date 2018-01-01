class Solution(object):
    #deal with reversed integer overflows, return 0, what is the limit of overflowing.
    #also, should deal with 123->321, 120->21, -123->-321
    def reverse(self,x):
        result = []
        term1 = 0
        if(x < 0):
            result.append('-')
            x = abs(x)
	    while(x % 10 != 0):

                term = x % 10
                result.append(str(term))
            x /= 10

	    print result

        #"".join(result)
    	#return ''.join(result)

if __name__ == "__main__":
    print Solution().reverse(12)