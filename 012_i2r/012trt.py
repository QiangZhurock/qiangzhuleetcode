class Solution(object):

    # solution, find the largest roman word v, and then num-v, shoule reduce time complextiy
    # find the range of x
    #time limited
    def find_range(self, num):
        """
        :type num: int
        :rtype: str
        """
        int2roman = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",

            10: "X",
            40: "XL",
            50: "L",
            90: "XC",

            100: "C",
            400: "CD",
            500: "D",
            900: "CM",

            1000: "M"
        }
        for ind, val in enumerate(int2roman):
            if (ind < len(int2roman) and val < num < int2roman[ind + 1]):
                return_ind, return_val = ind, val
            else:
                return 1000, "M"

    def intToRoman(self, num):
        list = []
        while (num != 0):
            x, v = self.find_range(num)
            num = num - x
            list.append(v)
        str1 = ''.join(list)
        return str1




