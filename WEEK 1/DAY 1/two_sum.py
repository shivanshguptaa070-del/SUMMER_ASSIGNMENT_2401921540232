class Solution(object):
    def twoSum(self, nums, target):
        
        
        d={}
        for i in range(len(nums)):
            sub=target-nums[i]
            if sub not in d:
                d[nums[i]]=i
            else:
                return (d[sub],i)
            