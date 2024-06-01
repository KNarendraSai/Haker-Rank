from collections import defaultdict
d = defaultdict(list)
n, m = map(int, input().split())
for i in range(1, n + 1):
    d[input()].append(i)
for j in range(m):
    s = input()
    if s in d:
        arr = d[s]
        for val in arr:
            print(val, end=" ")
        print()
    else:
        print(-1)