class Solution(object):
    #Since the array is already sorted.
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 
        index = 0
        nums[index] = nums[0]
        for i in xrange(1, len(nums)):
            if nums[index] != nums[i]:
                index += 1
                nums[index] = nums[i]
        print nums[0:index+1]    
        return index + 1
        