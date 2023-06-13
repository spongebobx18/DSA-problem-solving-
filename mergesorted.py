class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        length = m+n
        for i in range(length):
            if nums1[i] == 0:
                if len(nums2)!=0:
                    nums1.remove(nums1[i])
                    nums1.insert(i,nums2[0])
                    nums2.pop(0)
        nums1.sort()
