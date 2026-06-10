class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
       
        k = len(needle)

        for l in range(len(haystack) - k + 1):
            if haystack[l:l + k] == needle:
                return l

        return -1