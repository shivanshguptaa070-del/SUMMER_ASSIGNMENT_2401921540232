class Solution(object):
    def maxSubArray(self, nums):
    
     
        maxsum = nums[0]
        sum = 0

        for i in nums:
            sum += i

            if sum > maxsum:
                maxsum = sum

            if sum < 0:
                sum = 0

        return maxsum
        