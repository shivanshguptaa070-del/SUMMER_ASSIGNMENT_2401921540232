class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)
        st = []
        left = [-1] * n
        right = [n] * n
        for i in range(n):
            while st and heights[st[-1]] >= heights[i]:
                st.pop()
            if st:
                left[i] = st[-1]
            st.append(i)
        st = []
        for i in range(n - 1, -1, -1):
            while st and heights[st[-1]] >= heights[i]:
                st.pop()
            if st:
                right[i] = st[-1]
            st.append(i)
        ans = 0
        for i in range(n):
            width = right[i] - left[i] - 1
            area = heights[i] * width
            ans = max(ans, area)
        return ans