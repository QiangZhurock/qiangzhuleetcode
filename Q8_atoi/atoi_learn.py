# Time:  O(n)
# Space: O(1)
#
# Implement atoi to convert a string to an integer.
#
# Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below
# and ask yourself what are the possible input cases.
#
# Notes: It is intended for this problem to be specified vaguely (ie, no given input specs).
# You are responsible to gather all the input requirements up front.
#
# spoilers alert... click to show requirements for atoi.
#
# Requirements for atoi:
# The function first discards as many whitespace characters as necessary
# until the first non-whitespace character is found. Then, starting from this character,
# takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.
#
# The string can contain additional characters after those that
# form the integral number, which are ignored and have no effect on the behavior of this function.
#
# If the first sequence of non-whitespace characters in str is not a valid integral number,
# or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
#
# If no valid conversion could be performed, a zero value is returned.
# If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.
#
class Solution(object):
    def atoi(self, str):
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        if not str:
            return 0
        result = 0
        len_str = len(str)
        sign = 1
        i = 0
        while i < len_str and str[i].isspace():
            i += 1

        if str[i] == '+':
            i += 1
        elif str[i] == '-':
            sign = -1
            i += 1

        while i < len_str and '0' <= str[i] <= '9':
            a = int(str[i])
            result = result * 10 + a
            i += 1
        result = result * sign
        if (result > INT_MAX):
            return INT_MAX
        elif (result < INT_MIN):
            return INT_MIN
        else:
            return result

if __name__ == "__main__":
    print Solution().atoi("")
    print Solution().atoi("-1")
    print Solution().atoi("123")
    print Solution().atoi("2147483647")
    print Solution().atoi("2147483648")
    print Solution().atoi("-2147483648")
    print Solution().atoi("-2147483649")
