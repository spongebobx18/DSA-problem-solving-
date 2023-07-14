class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        start=0
        end=0
        result=[]
        for i in range (len(s)):
            end=max(end, s.rindex(s[i]))
            if i == end:
                result.append(end-start+1)
                start=i+1


        return result             
