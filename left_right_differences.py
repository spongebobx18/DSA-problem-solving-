class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n=len(nums)
        left = [0] * n
        right = [0] * n
        result = [0] * n

        left_sum = 0
        for i in range(len(nums)):
            left[i] = left_sum
            left_sum += nums[i]
        
        right_sum = 0
        for j in range(len(nums) - 1, -1, -1):
            right[j] = right_sum
            right_sum += nums[j]

        for t in range(len(left)):
            result[t] = abs(left[t] - right[t])

        return result