from collections import deque

n = int(input())
d = deque()

for _ in range(n):
    s = input().split()
    if s[0] == 'append':
        d.append(int(s[1]))
    elif s[0] == 'appendleft':
        d.appendleft(int(s[1]))
    elif s[0] == 'clear':
        d.clear()
    elif s[0] == 'extend':
        d.extend(map(int, s[1:]))
    elif s[0] == 'extendleft':
        d.extendleft(map(int, s[1:]))
    elif s[0] == 'count':
        print(d.count(int(s[1])))
    elif s[0] == 'pop':
        d.pop()
    elif s[0] == 'popleft':
        d.popleft()
    elif s[0] == 'remove':
        d.remove(int(s[1]))
    elif s[0] == 'reverse':
        d.reverse()
    elif s[0] == 'rotate':
        d.rotate(int(s[1]))
    else:
        print(f"Unknown command: {s[0]}")

print(" ".join(map(str, d)))