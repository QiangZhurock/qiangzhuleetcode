class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # two pointer, return i,j
        left = 0
        right = len(height) - 1
        maxarea = 0
        max_right = right
        max_left = left
        while (left < right):
            if (height[left] < height[right]):
                curarea = (right - left) * height[left]
                if maxarea < curarea:
                    maxarea = curarea
                    max_right = right
                left += 1
            else:
                curarea = (right - left) * height[right]
                if maxarea < curarea:
                    maxarea = curarea
                    max_left = left
                right -= 1
        return maxarea,max_left,max_right


if __name__ == "__main__":
    print Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
