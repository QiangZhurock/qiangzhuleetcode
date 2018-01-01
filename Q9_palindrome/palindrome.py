class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        x = str(x)
        lst = list(x)
        i = 0
        j = len(lst) - 1
        while (i < j and lst[i] == lst[j]):
            i += 1
            j -= 1
        if (i >= len(lst) / 2):  # 123 1221
            return True
        else:
            return False
        print lst
