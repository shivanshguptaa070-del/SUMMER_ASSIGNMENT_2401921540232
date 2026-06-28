# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.result = 0
        def solve(node):
            if not node:
                return 0
            left = solve(node.left)
            right = solve(node.right)
            self.result = max(self.result, left + right)
            return max(left, right) + 1
        solve(root)
        return self.result

