
from collections import OrderedDict
n=int(input())
invoice = OrderedDict()

for _ in range(n):

    data = input().split()
    price = int(data.pop())
    name = " ".join(data)
    invoice[name] = invoice.get(name, 0) + price
for name, price in invoice.items():
    print(name, price)