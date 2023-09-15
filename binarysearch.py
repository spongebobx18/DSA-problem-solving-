class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Check for infinite loop on two elements 
        # Handle integer overflow 
        low,high=0,len(nums)-1

        while(low<high):
            mid = low + (high-low)//2
            if(target <= nums[mid]  ):
                high = mid
            else:
                low = mid+1
        return low if nums[low]==target  else -1