"""
There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays. The overall
run time complexity should be O(log (m+n)).
Merge two arrays to get the median, O((m+n)/2)
"""
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # solution method is the same as Q2

        median = 0
        i = 0
        j = 0
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)
        len_total = len_nums1 + len_nums2
        if len_nums1 < len_nums2:
            return self.findMedianSortedArrays(nums2, nums1)
        num_result = []
        # after adding one condition, satisfy the (m+n)/2 time requirement.
        # sacrifice space to improve time.
        while (i < len_nums1 and (len(num_result) < len_total / 2 + 1)):
            if (j < len_nums2):
                if (nums1[i] < nums2[j]):
                    num_result.append(nums1[i])
                    i += 1
                else:
                    num_result.append(nums2[j])
                    j += 1
            else:
                num_result.append(nums1[i])
                i += 1

        # deal with the situation the same length, [1,2],[3,4] or [1,3],[2,4].
        while (j < len(nums2) and (len(num_result) < len_total / 2 + 1)):
            num_result.append(nums2[j])
            j = j + 1

        #t = 0
        #just use to debug, don't run this following program will improve running time.
        # while (t < len(num_result)):
        #   print num_result[t]
        #   t += 1
        # find  median:
        pivot = len_total / 2
        if len_total % 2 == 0:
            median = float((num_result[pivot - 1] + num_result[pivot]) / 2.0)  # divide 2.0
        else:
            median = num_result[pivot]
        return median

if __name__ == "__main__":
    median = Solution().findMedianSortedArrays([1,2], [3,4])
    print median