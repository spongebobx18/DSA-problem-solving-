class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        count = [0]*len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j!= i and nums[j] < nums[i]:
                    count[i]+=1
        return count