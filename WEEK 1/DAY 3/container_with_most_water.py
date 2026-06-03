class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        left = 0
        right = len(height) - 1

        areas = []

        while left < right:

            area = (right - left) * min(height[left], height[right])

            areas.append(area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max(areas)