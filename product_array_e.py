class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_prod = 1
        n = len(nums)
        res = [1]*n

        for i in range(n):
            res[i]*=pre_prod
            pre_prod*=nums[i]
        print(res)
            
        suff_prod = 1
        for i in range(n-1,-1,-1):
            res[i]*=suff_prod
            suff_prod*=nums[i]
            

        return res
            
            
            
