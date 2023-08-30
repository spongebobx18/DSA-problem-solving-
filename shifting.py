class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        alphabet='abcdefghijklmnopqrstuvwxyz'
        s=list(s)
        mop=len(s)
        summ=sum(shifts)
        
        for i in range(mop):

            sef= ord(s[i])-ord('a')  
            sef=sef+summ
            character=chr(ord("a") + sef%26)
            summ-=shifts[i]
            s[i]=character
        s=''.join(s)
        return s
