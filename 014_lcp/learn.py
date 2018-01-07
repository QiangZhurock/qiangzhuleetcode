"""
Write a function to find the longest common prefix string amongst an array of strings.
"""
__author__ = 'Danyang'


class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        l = min(map(len, strs))
        i = 0
        while i < l:
            ele = strs[0][i]
            for s in strs:
                if s[i] != ele:
                    return strs[0][:i]
            i += 1
        return strs[0][:i]

if __name__ == "__main__":
    strs = ["bca","dea"]
    print Solution().longestCommonPrefix(strs)