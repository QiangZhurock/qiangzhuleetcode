1. problem understanding:
	https://leetcode.com/problems/longest-common-prefix/discuss/6916
It seems that it is not to check between pair of strings but on all the strings in the array.
For example:
{“a”,“a”,“b”} should give “” as there is nothing common in all the 3 strings.
{“a”, “a”} should give “a” as a is longest common prefix in all the strings.
{“abca”, “abc”} as abc
{“ac”, “ac”, “a”, “a”} as a.
Logic goes something like this:
Pick a character at i=0th location and compare it with the character at that location in every string.
If anyone doesn’t have that just return “”
Else append that character in to the result.
Increment i and do steps 1-3 till the length of that string.
return result.
Make sure proper checks are maintained to avoid index out of bounds error.

IMPORTANT::
learn.py nice!!! !!!judge != firstly!!! 
match problem judge not equal, if not equal, return!!

2.error encountered
error1: input == [], should check this and return ""
error2: ["aca","cba"] should return "", however I return a, violate prefix.
	 add: len(result) in if(count == len(strs) - 1 and len(result) == i-1):
then error3: ["a"] return ""
	   add:        if(len(strs) == 1):
                	result.append(strs[0])
then error4:
	["c","c"] return ""
error: see lcp_try:
        ["a"],return aa
	trick or habit got if should with else
see successul_try2: deal with all the special cases firstly. multiple return!!

3. learn.py:
	learn the function:  l = min(map(len, strs))