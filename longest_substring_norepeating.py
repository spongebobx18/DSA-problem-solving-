class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left=0
        right=0
        maxx=0
        unique=set()
        while right<len(s):
              if s[right]not in unique:
                  unique.add(s[right])
                  maxx=max(maxx, right-left+1)
                  right+=1
              else:
                  unique.remove(s[left])

                  left+=1
        return maxx              


