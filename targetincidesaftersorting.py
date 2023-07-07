class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
        size=len(nums)
        ans=[]
        nums.sort()
        for i in range(size):
            if target==nums[i]:
                ans.append(i)
                return ans
