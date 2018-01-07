# -*- coding: utf-8 -*-
"""
Given an array S of n integers, are there elements a, b, c in S such that a +
b + c = 0? Find all unique triplets in the array which gives the sum of zero.
Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},
    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
"""


class Solution(object):
    def threeSum(self, num):
        """
        Brute force first, then determine whether sorting time complexity exceeds the brute force
        Three pointers
        Algorithm:
        1. sort everything first
        2. three pointers, i, j, k
        3. notice JUMP
        Palantir Technology Interview Question
        http://en.wikipedia.org/wiki/3SUM
        O(n^2)
        Notice:
        0. duplicated element will cause "Output Limit Exceeded" error
        1. avoid using set
        :param num: array
        :return: a list of lists of length 3, [[val1,val2,val3]]
        """

        # record result
        result = []
        num.sort()  # sorting first, avoid duplicate,
        i = 0
        while i < len(num)-2:
            j = i+1
            k = len(num)-1
            while j < k:
                lst = [num[i], num[j], num[k]]
                if sum(lst) == 0:
                    result.append(lst)
                    k -= 1
                    j += 1
                    # JUMP remove duplicate
                    while j < k and num[j] == num[j-1]:
                        j += 1
                    while j < k and num[k] == num[k+1]:
                        k -= 1
                elif sum(lst) > 0:
                    k -= 1
                else:
                    j += 1

            i += 1
            # remove duplicate
            while i < len(num)-2 and num[i] == num[i-1]:
                i += 1

        return result

if __name__ == "__main__":
    print Solution().threeSum([-1, 0, 1, 2, -1, -4])