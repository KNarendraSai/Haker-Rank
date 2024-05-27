
s = set(map(int, input().strip().split()))
N = int(input().strip())
for _ in range(N):
    command = input().strip().split()
    operation = command[0]

    if operation == "pop":
        s.pop()
    elif operation == "remove":
        element = int(command[1])
        if element in s:
            s.remove(element)
    elif operation == "discard":
        element = int(command[1])
        s.discard(element)


print(sum(s))
