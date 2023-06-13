class Solution:
    def missingNumber(self,nums):
        n = len(nums)
        expected_sum = (n * (n + 1)) // 2
        actual_sum = sum(nums)
    #actual sum from the expected sum will yield the missing number 
        return expected_sum - actual_sum
       