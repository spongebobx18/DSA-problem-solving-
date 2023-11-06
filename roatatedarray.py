class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums) # getting the length of the array 
        k = k % n  # for is k is greater than n 
        extracted_elements = nums[-k:] # getting till k 
        del nums[-k:] # 
        nums[:0] = extracted_elements
        return nums
        


      