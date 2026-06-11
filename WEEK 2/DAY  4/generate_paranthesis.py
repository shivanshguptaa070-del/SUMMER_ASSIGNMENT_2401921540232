class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        def bt(cur, op, cl):
            if len(cur) == 2 * n:
                ans.append(cur)
                return
            if op < n:
                bt(cur + "(", op + 1, cl)
            if cl < op:
                bt(cur + ")", op, cl + 1)
        bt("", 0, 0)
        return ans