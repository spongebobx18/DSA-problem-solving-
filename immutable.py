class NumArray:

    def __init__(self, nums: List[int]):
        nums=nums
        n=len(nums)
        p_s=[0]*n
        p_s[0]=nums[0]
        for i in range (1, n):
            p_s[i]=p_s[i-1]+nums[i]
        

        

    def sumRange(self, left: int, right: int) -> int:
        if left==0:
            return self.p_s[right]
        else:
            return self.p_s[right]-self.p_s[left-1]
        
        

        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)