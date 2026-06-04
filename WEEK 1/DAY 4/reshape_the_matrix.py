class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
"""

        rows = len(mat)
        cols = len(mat[0])

        if rows * cols != r * c:
            return mat

        nums = []

        for row in mat:
            for num in row:
                nums.append(num)

        result = []
        index = 0

        for i in range(r):
            temp = []

            for j in range(c):
                temp.append(nums[index])
                index += 1

            result.append(temp)

        return result