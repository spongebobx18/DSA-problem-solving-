class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ten=bisect.bisect_left(nums, target)
        print(ten)
        end=bisect.bisect_right(nums, target)
        print(end)
        if ten>end-1:
            return [-1, -1]
        else:
            return [ten, end-1]
        

        # left, right = 0, len(nums) - 1
        # count=0

        # while left <= right:
        #     mid = (left + right) // 2
        #     if nums[mid] == target:
        #         left=mid
        #         while nums[left]==target:
        #             count+=1

        #         return [mid+1, mid+count+1]  
        #     elif nums[mid] > target:
        #         right = mid - 1
        #     else:
        #         left = mid + 1

        # return [-1, -1]




        