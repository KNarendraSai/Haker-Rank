from collections import OrderedDict

n = int(input())
d = OrderedDict()

for _ in range(n):
    s = input()
    d[s] = d.get(s, 0) + 1

print(len(d))

for k in d:
    print(d[k], end=" ")