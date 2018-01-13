class Solution(object):
    def multiply(self, num1, num2):
        num1 = list(num1)[::-1]
        num2 = list(num2)[::-1]
        #num1[0]* num2[0] error
        num3 = [0 for _ in range(len(num1) + len(num2))] #should initialize firstly, or index out of range error.
        for i in xrange(0, len(num1)):
            for j in xrange(0, len(num2)):
                num3[i+j] += int(num1[i]) * int(num2[j])
        for p in xrange(0, len(num3)):
            if num3[p] > 9:
                num3[p+1] += num3[p] // 10
                num3[p] = num3[p] % 10
        num3.reverse() #the elements in num3 are int type
        #result = ''.join(num3)
        #result = ''.join(str(num3))

        #print num3
        #result = []
        result = ''.join(str(n) for n in num3) #string
        print result
        #return str(result) error
        return str(int(result)) #convert to int then convert to str, need to return str


if __name__ == "__main__":
    str1 = "0"
    str2 = "0"
    print Solution().multiply(str1, str2)



