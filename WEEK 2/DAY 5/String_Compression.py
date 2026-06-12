class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        
        i = 0
        w = 0

        while i < len(chars):
            ch = chars[i]
            cnt = 0

            while i < len(chars) and chars[i] == ch:
                cnt += 1
                i += 1

            chars[w] = ch
            w += 1

            if cnt > 1:
                for c in str(cnt):
                    chars[w] = c
                    w += 1

        return w
        