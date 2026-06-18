class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        st = []
        for x in tokens:
            if x not in "+-*/":
                st.append(int(x))
            else:
                a = st.pop()
                b = st.pop()
                if x == "+":
                    st.append(b + a)
                elif x == "-":
                    st.append(b - a)
                elif x == "*":
                    st.append(b * a)
                else:
                    st.append(abs(b) // abs(a) * (1 if b*a >= 0 else -1))
        return st[-1]
