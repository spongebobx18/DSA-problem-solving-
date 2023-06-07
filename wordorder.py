# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
N = int(input())

list1 = []
for i in range(N):
    text = input()
    list1.append(text)

count = Counter(list1)   
list1 = list(set(list1))

print(len(list1))

new_list =[]
for key in count:
    new_list.append(count[key])

print(*new_list)