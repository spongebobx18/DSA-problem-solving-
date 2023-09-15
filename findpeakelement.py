class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        # n=len(nums)
        # for i in range(n):
        #     if nums[i-1]<nums[i] and nums[i+1]<nums[i]:
        #         return i
        n=len(nums)
        if n==1 :
            return 0
        elif nums[n-1]>nums[n-2]:
            return n-1
        l,h=0,n-1
        while l<=h:
            m=(l+h)//2
            if nums[m]>nums[m+1] and nums[m]>nums[m-1]:
                return m
            elif nums[m]>nums[m+1]:
                h=m-1
            else:
                l=m+1 
        

        