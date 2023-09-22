class Solution:
    def findMin(self, nums: List[int]) -> int:
        hi, lo = len(nums) - 1, 0
        while hi - 1 > lo:
            mid = (hi + lo)//2
            if nums[lo] > nums[mid]: 
                hi = mid
            else: 
                lo = mid

        if nums[hi] > nums[lo]:
            return nums[0]
        return nums[hi]