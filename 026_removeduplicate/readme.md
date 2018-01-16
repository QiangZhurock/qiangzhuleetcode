0. Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length. Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory. Given nums = [1,1,2],Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.
1. forget special case, nums==[]
2. remember that the array has been sorted.
3. print nums[0:index+1] +1!!