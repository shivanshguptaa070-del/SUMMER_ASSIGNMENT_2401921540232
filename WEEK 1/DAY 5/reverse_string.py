class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        #aise kr skte hai but yeh direct function lagake ho jayega so isse hum without function ke liye two pointer kr skte 
       # return s.reverse()
   

        l = 0
        r = len(s) - 1

        while l < r:

            s[l], s[r] = s[r], s[l]

            l += 1
            r -= 1