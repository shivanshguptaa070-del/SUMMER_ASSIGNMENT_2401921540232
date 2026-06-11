class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        c = s.split()  
        for i in range(len(c)):
            c[i] = c[i][::-1]
        return " ".join(c)