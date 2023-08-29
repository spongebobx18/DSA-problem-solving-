class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n=len(nums)
        result=[]
        for i in range (n):
            summ=0
            for j in range (i+1):
                summ+=nums[j]
            result.append(summ)
        return result
