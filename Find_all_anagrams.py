class Solution(object):
    def findAnagrams(self, s, p):
        res = []
        c = Counter(p)
        pip=len(p)
        pop=len(s)
        cur = Counter(s[:pip])
        for i in range(pop-pip+1):
            if cur==c:
                res.append(i)
            if i == pop-pip:
                break
            cur[s[i]]-=1
            if cur[s[i]]==0:
                del cur[s[i]]
            cur[s[i+pip]]+=1
        return res