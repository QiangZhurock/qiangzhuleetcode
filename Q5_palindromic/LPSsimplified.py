"""
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and
there exists one unique longest palindromic substring.
"""
from __future__ import  print_function
import sys
sys.stdout.write('')

## http://www.cse.iitd.ac.in/~rjaiswal/2017/COL106/Homework/hw-12-soln.pdf
class Solution(object):
    def longestPalindrome(self, s):
        """
        O(n^2)
        :param s: string
        :return: string
        """
        len_s = len(s)
        # Creates a list containing 5 lists, each of 8 items, all set to 0
        w, h = len(s), len(s)
        l = [[0 for x in range(w)] for y in range(h)]
        p = [[0 for x in range(w)] for y in range(h)]
        #how to think. just write down a 4*4 matrix, and find the rule. Eg:[0,1],[1,2],[2,3];
        #[0,2],[1,3]; [0,3]. we find that i from 0 to len_s - 1/2/3
        for i in range(len_s):
            l[i][i] = 1
        for t in range(1, len_s):
            for i in range(len_s - t):
                j = i + t
                if (s[i] == s[j] ):
                    if(s[i+1] == s[j-1]):
                        l[i][j] = l[i + 1][j - 1] + 2 #cause problem, this is used to find subsecquence
                        p[i][j] = 1 #from south-west
                    else:
                        l[i][j] = 1
                        p[i][j] = 4
                else: #write like this is clear and better.
                    if(l[i+1][j] > l[i][j-1]):
                        l[i][j] = l[i+1][j]
                        p[i][j] = 2 #from south
                    else:
                        l[i][j] = l[i][j - 1]
                        p[i][j] = 3 #from west
        for i in range(len_s):
            for j in range(len_s):
                print (l[i][j], end = '')
                if j == len_s - 1:
                    print ('\n')
        return self.printsubstring(s,len_s,p) #use self.print, or cannot find it. def also need to add self as argument

    #find the substring
    def printsubstring(self,s,len_s,p):
        i = 0
        j = len_s - 1
        k = 0
        #don't need result finally, the key is to find the middle element i and half length k.
        while(i < j): #why?--upper part of the matrix
            if(p[i][j] == 1 ):
                k = k+1
                i = i + 1
                j = j - 1
            else:
                if(p[i][j] == 2):
                    i = i + 1
                    k = 0
                else:
                    j = j - 1
                    k = 0
        print (k)
        #for j in range(i-k,i+k+1):
         #   print (s[j])
        if (i == j):
            return s[i-k: i+k+1] #i+k+1 instead of i+k
        else:
            return s[i-k: i+k]
	#from iit blog
	#For s = 1 to k − 1 
	#Print(A[s])
	#If (i = j)Print(S[i]) 
	#For s = k − 1 to 1
	#Print(A[s])
if __name__ == "__main__":
    result = []
    result = Solution().longestPalindrome("abadada") #== "aaabbbaaa"
    print (result)