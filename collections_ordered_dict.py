from collections import OrderedDict
d = OrderedDict()
n = int(input())
for _ in range(n):
    s = input().split()
    item_name = " ".join(s[:-1])
    net_price = int(s[-1])  # The last part is the net price
    d[item_name] = d.get(item_name, 0) + net_price
for k in d:
    print(k, d[k])