class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        min_distance = 10000000000000000
        min_sum = 0
        nums.sort()
        i = 0
        while i < len(nums) - 2:
            j = i + 1
            k = len(nums) - 1
            while j < k:
                lst = [nums[i], nums[j], nums[k]]
                cur_sum = sum(lst)
                cur_distance = abs(cur_sum - target)
                if cur_distance < min_distance:
                    min_distance = cur_distance
                    min_sum = cur_sum
                    if min_distance == 0:
                        return min_sum

                elif cur_sum > target:
                    k -= 1
                else:
                    j += 1
            i += 1
        return min_sum


if __name__=="__main__":
    print Solution().threeSumClosest([0, 1, 2], 3)



