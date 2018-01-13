class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # write your code here
        num1 = list(num1)[::-1]
        num2 = list(num2)[::-1]
        num3 = [0 for _ in range(len(num1) + len(num2))]

        # need to learn, nice method
        for i in range(len(num1)):
            for j in range(len(num2)):
                num3[i + j] += int(num1[i]) * int(num2[j])

        for i in range(len(num3)):
            if num3[i] > 9:
                num3[i + 1] += num3[i] // 10 #""" x.__floordiv__(y) <==> x//y """
                num3[i] %= 10
        print num3
        res = ''.join(str(n) for n in num3[::-1])

        return str(int(res))

if __name__ == "__main__":
    solution = Solution()
    #print solution.add([2, 1], [9])
    print solution.multiply("123", "456")
    print solution.multiply("123", "999")
    print solution.multiply("0", "0")
    print "23"
