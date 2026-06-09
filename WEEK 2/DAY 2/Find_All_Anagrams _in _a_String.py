class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
        if len(p) > len(s):
            return []

        x = {}
        y = {}
        ans = []

        for c in p:
            x[c] = x.get(c, 0) + 1

        for i in range(len(p)):
            y[s[i]] = y.get(s[i], 0) + 1

        if x == y:
            ans.append(0)

        l = 0

        for r in range(len(p), len(s)):
            y[s[r]] = y.get(s[r], 0) + 1

            y[s[l]] -= 1
            if y[s[l]] == 0:
                del y[s[l]]

            l += 1

            if x == y:
                ans.append(l)

        return ans