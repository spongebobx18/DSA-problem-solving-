class Solution:
    def interpret(self, chk: str) -> str:
        chk = chk.replace("()", "o")
        chk = chk.replace("(al)", "al")
        return chk