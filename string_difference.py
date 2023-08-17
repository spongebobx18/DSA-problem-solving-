class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        sPtr, tPtr = 0,0
        while sPtr<len(s) and tPtr<len(t):
            if s[sPtr]==t[tPtr]:
                 tPtr += 1
            sPtr+=1
        return len(t)-tPtr