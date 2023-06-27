class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n= len(arr)
        max_element = -1
        for i in range(n-1, -1, -1):
            
            current = arr[i]
            arr[i] = max_element

            if current>max_element:
                max_element=current
        return arr