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
        while (left < right):
            curarea = min(height[left], height[right]) * (right - left)
            maxarea = max(maxarea, curarea)
            if (height[left] < height[right]):
                left += 1
            else:
                right -= 1
        return maxarea

if __name__ == "__main__":
    print Solution().maxArea([2,3,1])
