class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pr_sum = [0] * (len(nums)+1)
        for i in range(1, len(pr_sum)):
            pr_sum[i] = pr_sum[i-1] + nums[i-1]
        
        dic = dict()
        count = 0
        for i in range(len(pr_sum)):
            if (pr_sum[i] % k) in dic:
                count += dic.get(pr_sum[i] % k)
            dic[pr_sum[i] % k] = dic.get(pr_sum[i]%k, 0) + 1
        return count