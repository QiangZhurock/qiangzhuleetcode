"""
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and
there exists one unique longest palindromic substring.
"""
from __future__ import  print_function
import sys
sys.stdout.write('')

#method1:
#see readme for details.
class Solution(object):
    def longestPalindrome_extending(self, s):
        result = s[0] #initialize, and also if the LPS is only one, return first character.
        len_s = len(s)
        for i in range(len_s):
            #even length
            #if (len_s % 2 == 0):
               # cur = self.get_palindrome_from_center(s, i, i+1)
                #if len(cur) > len(result):
                 #   result = cur
            # odd length
           # else:
	          #  cur = self.get_palindrome_from_center(s, i, i)
	           # if len(cur) > len(result):
		        #    result = cur

            #palindrome has odd lengthdf, like "aba"
            cur = self.get_palindrome_from_center(s, i, i)
            if len(cur) > len(result):
                result = cur
            #palindrome has even length, like "abba"
            cur = self.get_palindrome_from_center(s, i, i + 1)
            if len(cur) > len(result):
                result = cur
        return result

    def get_palindrome_from_center(self, s, begin, end):
	    left = begin
	    right = end
	    length = 0
	    while(left >=0 and right < len(s) and s[left] == s[right]): #a mistake use if again!!
	        left -= 1
	        right += 1
	        length += 1
	    return s[left + 1: right -1 +1] #attention, left+1,because, when left + 1, we break the while loop.
        #return s[left + 1: left + 2*length]]  # attention, left+1,because, when left + 1, we break the while loop.


    def longestPalindrome_dp(self, s):
        fs
if __name__ == "__main__":
    result = []
    result = Solution().longestPalindrome_extending("abcb") #== abcd
    print (result)



