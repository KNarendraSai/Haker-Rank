import math
import os
import random
import re
import sys
if __name__ == '__main__':
    s = input()
d = {}
for char in s:
    d[char] = d.get(char, 0) + 1
sorted_items = sorted(d.items(), key=lambda x: (-x[1], x[0]))
for i, k in sorted_items[:3]:
    print(i, k)