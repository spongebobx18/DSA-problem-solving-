class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        dur = 0
        i = 0
        p=len(tickets)
        while tickets[k] != 0:
            if tickets[i] != 0:
                tickets[i] -= 1
                dur += 1

            i = (i+1)%p

        return dur