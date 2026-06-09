
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
       
        if len(s1) > len(s2):
            return False

        cnt1 = {}
        cnt2 = {}

        for ch in s1:
            cnt1[ch] = cnt1.get(ch, 0) + 1

        for i in range(len(s1)):
            cnt2[s2[i]] = cnt2.get(s2[i], 0) + 1

        if cnt1 == cnt2:
            return True

        l = 0

        for r in range(len(s1), len(s2)):
            cnt2[s2[r]] = cnt2.get(s2[r], 0) + 1

            cnt2[s2[l]] -= 1
            if cnt2[s2[l]] == 0:
                del cnt2[s2[l]]

            l += 1

            if cnt1 == cnt2:
                return True

        return False