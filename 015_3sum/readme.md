2. see learnbetter.py---> TLE???

	thought is good, the same as 3sum_learn.
	2.1 sort the array.
	2.2 ind i in xrange(0, len(nums) - 2)
	2.3 j,k and save three val then judge their sum.
3. tryafterlearn.py, still TLE ???
4. 3sum_learn.py AC

1. thought intuitively!
The way to think about it is since it’s 3 sum, there’s only going to be 3 numbers.
	 So to find the combinations of 3 numbers, he is iterating through the list with the first pointer, and then trying to find two extra numbers to sum to 0.
 	Since the list is ordered, the right pointer will always be higher than the middle pointer. So if the sum is too large, you can move the right pointer back one. On the other hand, if the sum is too small (below 0), then move the middle pointer up one.

