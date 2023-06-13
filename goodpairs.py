class Solution:
    def numIdenticalPairs(self, nums):
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1  
        good_pairs = 0
        for count in counts.values():
            good_pairs += count * (count - 1) // 2
        return good_pairs
