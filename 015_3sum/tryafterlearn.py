
class Solution(object):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    def threeSum(self, nums):
        nums.sort() # sorting first, avoid duplicate,
        i = 0
        result = []
        len_nums = len(nums)
        for i in xrange(len_nums - 2):
            if i > 0 and nums[i] == nums[i - 1]: #deal with duplicate
                continue
            left = i + 1
            right = len_nums - 1
            while (left < right):
                lst = [nums[i], nums[left], nums[right]]
                sum_lst = sum(lst)
                if sum_lst == 0:
                    result.append(lst)
                    left += 1
                    right -= 1
                    #deal with duplicate
                    while(left < right and nums[left] == nums[left - 1]):
                        left += 1
                    while(left < right and nums[right] == nums[right + 1]):
                        right += 1
                elif sum_lst > 0:
                    right -= 1
                else:
                    left += 1
        return result
if __name__ == "__main__":
    print Solution().threeSum([-1, 0, 1, 2, -1, -4])
