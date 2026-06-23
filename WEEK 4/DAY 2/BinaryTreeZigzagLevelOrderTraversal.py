# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        q = [root]
        left = True
        while q:
            temp = []
            n = len(q)
            for i in range(n):
                cur = q.pop(0)
                temp.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

            if not left:
                temp.reverse()

            res.append(temp)
            left = not left

        return res