class Solution(object):
    def dailyTemperatures(self, t):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
       #ISME TLE AA RHA HAI 
        """ 
        ans = [0] * len(t)

        for i in range(len(t)):
            for j in range(i + 1, len(t)):
                if t[j] > t[i]:
                    ans[i] = j - i
                    break

        return ans"""
        ans = [0] * len(t)
        st = []
        for i in range(len(t)):
            while st and t[i] > t[st[-1]]:
                idx = st.pop()
                ans[idx] = i - idx
            st.append(i)
        return ans