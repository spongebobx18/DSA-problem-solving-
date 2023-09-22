class Solution:
    def findMin(self, nums: List[int]) -> int:
        right, left = len(nums) - 1, 0
        while right - 1 > left:
            mid = (right + left)//2
            if nums[left] > nums[mid]: 
                right = mid
            else: 
                left = mid

        if nums[right] > nums[left]:
            return nums[0]
        return nums[right]
