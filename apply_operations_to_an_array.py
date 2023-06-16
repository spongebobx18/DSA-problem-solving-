class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        nums=[]
        for i in range (len(nums)-1):
            if nums[i]==nums[i+1]:
               nums*=2
               nums[i+1]=0
               zeros=nums.count(0)#count the number of zeros to append to the nums array later 

            nums=[number for number in nums if number!=0]#only add numbers that are not zero to the array 
            for i in range(zeros):
                nums=nums.append(zeros)# add the zeros to the arrays 
            return nums    