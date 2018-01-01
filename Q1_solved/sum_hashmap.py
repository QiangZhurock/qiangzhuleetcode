class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #create hash table
	hashmap = {}
   	for index, val in enumerate(nums):
		hashmap[val] = index
	
	#calculate
	for index, val in enumerate(nums):
		if (target - val) in hashmap:
			index2 = hashmap[target - val]
			if index2 != index:
				return index,index2