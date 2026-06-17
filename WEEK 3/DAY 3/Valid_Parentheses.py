class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st = []
        d = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        for ch in s:
            if ch in "([{":
                st.append(ch)
            else:
                if not st:
                    return False
                if st[-1] == d[ch]:
                    st.pop()
                else:
                    return False
        return len(st) == 0