class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
   
        Set = set()
        l = 0
        m = 0

        for r in range(len(s)):
            while s[r] in Set:
                Set.remove(s[l])
                l += 1

            Set.add(s[r])
            m = max(m, r - l + 1)

        return m