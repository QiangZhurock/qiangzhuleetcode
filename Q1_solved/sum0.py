class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        resultlist = []
        for i in range (len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i]+nums[j])==target:
                    resultlist.append(i)
                    resultlist.append(j)
        if(len(resultlist)!=0):
            print resultlist
            return resultlist
        else:
            print "error"
        