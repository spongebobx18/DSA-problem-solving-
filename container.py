class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        maximum=float("-inf")

        while left < right:
            maximum=max(maximum, min(height[left], height[right])*(abs(left-right)))
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maximum