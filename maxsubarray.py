class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        window = set()
        l = 0
        res = 0
        total = 0
        for r in range(len(nums)):
            total +=nums[r]
            if (r-l+1) > k:
                window.remove(nums[l])  
                total-=nums[l]
                l+=1
            while nums[r] in window:
                window.remove(nums[l])
                total-=nums[l]
                l+=1
            window.add(nums[r])
            if (r-l+1) == k:
                res = max(res,total)
            
        return res 