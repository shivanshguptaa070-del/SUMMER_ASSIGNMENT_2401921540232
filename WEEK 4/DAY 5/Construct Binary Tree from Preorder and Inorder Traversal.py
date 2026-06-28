class Solution:
    def buildTree(self, preorder, inorder):
        self.idx = 0
        
        def solve(start, end):
            if start > end:
                return None
            root_val = preorder[self.idx]
            i = start
            while i <= end:
                if inorder[i] == root_val:
                    break
                i += 1
            self.idx += 1
            root = TreeNode(root_val)
            root.left = solve(start, i - 1)
            root.right = solve(i + 1, end)            
            return root
        return solve(0, len(preorder) - 1)
