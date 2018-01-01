"""
Given a string, find the length of the longest substring without repeating characters. For example, the longest
substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring
is "b", with the length of 1.
"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        Algorithm: Hash Map, two pointers
        Hash Map: array visited = [] for all ascii, notice the algorithm of updating this array
        Two pointers: start - start of the string; ind - scanning
        Given a string, find the length of the longest substring without repeating characters.

        the basic idea is, keep a hashmap which stores the characters in string as keys and their
        positions as values,  and keep two pointers which define the max substring. move the right pointer to
        scan through the string , and meanwhile update the hashmap. If the character is already in the hashmap,
        then move the left pointer to the right of the same character last found.
        Note that the two pointers can only move forward.

        need to un-mark since in a new start the formal characters become unvisited again!!
        :param s: String
        :return: Integer
        """
        # last visited index in the string
        visited_last_index = [-1 for i in range(256)]  # ascii
        longest_length = 0  # record result

        start = 0  # pointer
        for ind, val in enumerate(s):
            ascll_number = ord(val)
            if (visited_last_index[ascll_number] == -1):
                longest_length = max(longest_length, ind - start + 1)
            else:
                longest_length = max(longest_length, (ind - 1) - start + 1 )
                #unmark the formal visited state
                #need to un-mark since in a new start the formal characters become unvisited again!!
                for i in range (start, visited_last_index[ascll_number]):
                    visited_last_index[ord(s[i])] = -1
                #update start, move start to the right, since tam is 3, am is 2, move start to 3!
                start = visited_last_index[ascll_number] + 1

            visited_last_index[ascll_number] = ind

        return longest_length

if __name__ == "__main__":  
    s = "tammxat"
    print Solution().lengthOfLongestSubstring(s)