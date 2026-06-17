class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        for x in nums1:
            idx = nums2.index(x)
            found = -1
            for i in range(idx + 1, len(nums2)):
                if nums2[i] > x:
                    found = nums2[i]
                    break
            ans.append(found)
        return ans