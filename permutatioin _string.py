class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        from collections import Counter
        freq_s1 = Counter(s1)
        window = Counter(s2[:len(s1)])
        for i in range(len(s1), len(s2)):
            if window == freq_s1:
                return True
            window[s2[i - len(s1)]] -= 1
            if window[s2[i - len(s1)]] == 0:
                del window[s2[i - len(s1)]]
            window[s2[i]] += 1
        
        return window == freq_s1
