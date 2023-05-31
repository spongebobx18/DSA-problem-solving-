
from collections import Counter

no_shoes = int(input())
shoe_sizes = list(map(int, input().split()))


counter_list = Counter(shoe_sizes)

no_customers = int(input())
total = 0

for _ in range(no_customers):
    size, price = tuple(map(int,input().split()))
    if size in counter_list.keys():
        if counter_list[size] >0:
            counter_list[size] = counter_list.get(size, 0) -1
            total += price
    

print(total)