class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        smallest = letters[0]
        l, r = 0, len(letters) - 1

        while l <= r:
            m = l + (r - l) // 2
            if ord(letters[m]) <= ord(target):
                l = m + 1
            else:
                smallest = letters[m]
                r = m - 1
            
        while smallest == target and smallest < letters[-1]:
            smallest = chr(ord(smallest) + 1)

        return smallest