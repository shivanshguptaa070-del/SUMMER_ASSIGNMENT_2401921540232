# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root):
        self.maxSum = float('-inf')
        self.solve(root)
        return self.maxSum
    
    def solve(self, root):
        if root is None:
            return 0
        l = self.solve(root.left)
        r = self.solve(root.right)
        neeche_hi_milgaya_answer = l + r + root.val
        koi_ek_acha = max(l, r) + root.val
        only_root_acha = root.val
        
        self.maxSum = max(self.maxSum, neeche_hi_milgaya_answer, koi_ek_acha, only_root_acha)
        
        return max(koi_ek_acha, only_root_acha)