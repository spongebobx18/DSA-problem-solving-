class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        comp = min(strs, key=len)

        for i, letter in enumerate(comp):
            for w in strs:
                if w[i] != letter:
                   return comp[:i]

        return comp
            
            