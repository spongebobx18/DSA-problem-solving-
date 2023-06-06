
def isAlienSorted(self, words: list[str], order: str) -> bool:
    alienMap = {n:i for i,n in enumerate(order)}

    for i in range(len(words)-1):
        w1,w2 = words[i],words[i+1]
        for j in range(len(w1)):
            if len(w2) == j:
                return False
            if w1[j] != w2[j]:
                if alienMap[w1[j]] > alienMap[w2[j]]:
                    return False 
                break

    return True
 
                    