# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

two = input().split()
T = int(two[0])
wo = int(two[1])
joinm = defaultdict(list)
for i in range(T):
    letter = input()
    joinm[letter].append(str(i+1))
for j in range(wo):
    word = input()
    if joinm[word]:
        print(" ".join(joinm[word]))
    else:
        print(-1)
            
