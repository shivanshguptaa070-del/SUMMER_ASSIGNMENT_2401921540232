class Solution(object):
    def removeDuplicates(self, nums):
        
        
        if len(nums) == 0:
            return 0

        s = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[s] = nums[i]
                s+= 1

        return s