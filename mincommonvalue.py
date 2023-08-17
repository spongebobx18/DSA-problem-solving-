class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        num1Ptr = 0
        num2Ptr = 0
        while num1Ptr<len(nums1) and num2Ptr<len(nums2):
            if nums1[num1Ptr] == nums2[num2Ptr]:
                return nums1[num1Ptr]
            elif nums1[num1Ptr] > nums2[num2Ptr]:
                num2Ptr+=1
            elif nums1[num1Ptr] < nums2[num2Ptr]:
                num1Ptr+=1
        return -1