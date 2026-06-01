class Solution(object):
    def findMaxAverage(self, nums, k):
       

        fsum  = sum(nums[:k])
        maxsum = fsum

        for i in range(k, len(nums)):
            fsum = fsum + nums[i] - nums[i - k]

            if fsum > maxsum:
                maxsum = fsum

        return float(maxsum) / k